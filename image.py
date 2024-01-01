import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImageReader, QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5 import QtCore
import pyqtgraph as pg
import logging

logging.basicConfig(filename = 'debugging.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', filemode='w')

class Image():
    #Global Variables
    image_instances = []
    max_width = 350
    max_height = 300
    ID = 0
    
    def __init__(self):
        self.first_time = True
        self.id = Image.ID
        Image.ID +=1
        self.path = None
        self.original_img = None  # Store the original image data (NumPy array)
        self.img = None  # for display only
        self.inner_img, self.outer_img = None, None
        # self.displayed_after_reshape = False  # Flag to track if displayed after reshape
        self.label = None  # QLabel containing Image
        self.spectrum_widget = None # QLabel Containing the Spectrums
        self.checkbox = None #Checkbox for outer region
        self.image_view = None
        self.image_item = None
        self.shape = None
        self.ft_roi = None
        self.fft_components = []

        #Image Components
        self.fft, self.fft_shift = None, None
        self.phase, self.phase_shifted = None, None
        self.mag, self.mag_shifted = None, None
        self.real, self.real_shifted= None, None
        self.imag, self.imag_shifted = None, None
        Image.image_instances.append(self)

    def get_id(self):
        return self.id

    def browse_file(self, label, spectrum_widget,checkbox):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        path, _ = QFileDialog.getOpenFileName(None, "Browse Image File", "", "Images (*.png *.jpg *.bmp *.gif *.tif *.tiff);;All Files (*)", options=options)
        if path:
            self.spectrum_widget = spectrum_widget
            self.checkbox = checkbox
            self.init_spectrum()
            self.set_file_path(path, label)
        self.first_time = True   

    def set_file_path(self, path, label):
        self.path = path
        self.load_image(path, label)

    def load_image(self, path, label):
        try:
            # Read and convert the image
            self.original_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE).astype(np.uint8)
            self.label = label
            self.reshape(self.original_img.shape[0], self.original_img.shape[1])
            self.reshape_all()
            
            # Convert to uint8 and scale pixel values
            self.original_img = self.original_img.astype(np.uint8)
            cv2.normalize(self.original_img, self.original_img, 0, 255, cv2.NORM_MINMAX)

            # Convert to QImage
            self.img = self.qimage_from_numpy(self.original_img)
            
            self.analyze_frequency_content()
            self.display_image(label)

        except cv2.error as e:
            logging.error(f"Couldn't load the image at {path}. OpenCV error: {str(e)}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")

    def display_image(self, label):
        """
        Display the image on the specified QLabel.

        Parameters:
        - label (QLabel): The QLabel where the image is going to be displayed.

        Returns:
        - None
        """
        self.original_img = self.original_img.astype(np.uint8)
        cv2.normalize(self.original_img, self.original_img, 0, 255, cv2.NORM_MINMAX)
        
        # Set the original and current images as QPixmap
        self.img = self.qimage_from_numpy(self.original_img)
        
        # Check if the image is not None
        if self.img is not None:
            # Set the pixmap only if the image is not None
            label.setPixmap(self.img)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def init_spectrum(self):
        self.spectrum_widget.clear()
        self.image_view = self.spectrum_widget.addViewBox()
        self.image_view.setAspectLocked(True)
        self.image_view.setMouseEnabled(x=False, y=False)

        # Create the ImageItem and set it to self.image_item
        self.image_item = pg.ImageItem()
        self.image_view.addItem(self.image_item)
        self.image_item.setTransform(pg.QtGui.QTransform().rotate(90))
        # Set the viewRange to cover the entire image
        # self.image_view.setRange(xRange=[-150, 0], yRange=[-1, 170])
    

        # Creating ROI 
        if self.id == 0:
            self.ft_roi = pg.ROI(pos = self.image_view.viewRect().center(), size = (50, 50), hoverPen='r', 
                        resizable= True, invertible= True, movable=True,
                        rotatable= False)
        else:
            self.ft_roi = pg.ROI(pos = self.image_view.viewRect().center(), size = (50, 50), hoverPen='r', 
                        resizable= True, invertible= True, movable=False, 
                        rotatable= False)
                
        self.image_view.addItem(self.ft_roi)
        self.add_scale_handles_ROI()

        
        # Connecting ROI signal to update region of data selected
        self.ft_roi.sigRegionChangeFinished.connect(lambda: self.region_update())
    
    #ZWDTHA
    def sync_roi_position(self, reference_roi):
        if self.ft_roi is not None:
            self.ft_roi.setPos(reference_roi.pos())
    
    # def connect_roi_movement(self, reference_roi):
    #     if self.ft_roi is not None and other_img.ft_roi is not None:
    #         # Connect the signal of this ROI to update the other ROI
    #         self.ft_roi.sigRegionChanged.connect(lambda: other_img.sync_roi_position(self.ft_roi))
    

    def reshape(self, img_height, img_width):
        """
        Resize the image to the specified dimensions.
        """
        new_height = min(Image.max_height, img_height)
        new_width = min(Image.max_width, img_width)
        Image.max_height = new_height
        Image.max_width = new_width

        # Resize the image
        self.original_img = cv2.resize(self.original_img, (new_width, new_height))
        # Update the shape attribute
        self.shape = self.original_img.shape

    @classmethod
    def reshape_all(self):
        """
        Resize all images in a list of Image instances to the smallest dimensions among them.
        """
        # Find the smallest image dimensions among all instances
        min_height = min(img.original_img.shape[0] for img in Image.image_instances if img.original_img is not None)
        min_width = min(img.original_img.shape[1] for img in Image.image_instances if img.original_img is not None)
        self.max_height, self.max_width = min_height, min_width
        # Resize all images to the smallest dimensions
        for img in Image.image_instances:
        
            try:
                if img.original_img is not None:
                    # img.reshape(Image.min_height, Image.min_width)
                    img.original_img = cv2.resize(img.original_img, (min_width, min_height))
                    img.shape = img.original_img.shape
                    img.display_image(img.label)
                    img.analyze_frequency_content()
            except Exception as e:
                logging.error(f"Error in instance {img.get_id()}: {type(e).__name__} - {str(e)}")

    def analyze_frequency_content(self):
       
        # Compute the 2D Fourier Transform
        self.fft = np.fft.fft2(self.original_img)

        # Shift the zero-frequency component to the center
        self.fft_shift = np.fft.fftshift(self.fft)
        logging.debug("fft shifted shape: %s Original shape: %s", self.fft_shift.shape, self.original_img.shape)

        # Compute the magnitude of the spectrum
        self.mag = np.abs(self.fft)
        self.mag_shifted = np.abs(self.fft_shift)

        # Compute the phase of the spectrum
        self.phase = np.angle(self.fft)
        self.phase_shifted = np.angle(self.fft_shift)

        # real ft components
        self.real = np.real(self.fft)
        self.real_shifted = np.real(self.fft_shift)

        #imaginary ft components
        self.imag = np.imag(self.fft)
        self.imag_shifted = np.imag(self.fft_shift)

        # Compute the components of the shifted Fourier Transform
        self.fft_components = [np.multiply(np.log(self.mag_shifted+1),20), self.phase_shifted, self.real_shifted, self.imag_shifted]

        #construct a dictionary to map each component to its type
        self.fft_dict = {
                        "FT Magnitude": self.fft_components[0],
                        "FT Phase": self.fft_components[1],
                        "FT Real": self.fft_components[2],
                        "FT Imaginary": self.fft_components[3]}

        
        self.plot_spectrum("FT Magnitude") 

    def plot_spectrum(self, spectrum_type):
        print("type after: ", spectrum_type)
        if spectrum_type in self.fft_dict:
            # Retrieve the corresponding spectrum from the dictionary
            spectrum = self.fft_dict[spectrum_type]
            logging.info(f"The type is {spectrum_type} and its values are: {spectrum[0][:5]}, its shape is: {spectrum.shape}")

            # Normalize the spectrum values to be between 0 and 255
            spectrum_normalized = ((spectrum - spectrum.min()) / (spectrum.max() - spectrum.min()) * 255).astype(np.uint8) 
            if self.first_time:
                self.first_time = False
                self.image_item.setImage(spectrum_normalized)
        else:
            logging.error(f"Error: Spectrum type '{spectrum_type}' not found in the dictionary.")
     
    def connect_checkbox(self, checkbox):
        checkbox.stateChanged.connect(lambda state, img=self: img.region_update())

    def change_brightness(self, brightness_factor):      
       # Change the brightness of the image
        logging.debug(f'Brightness Factor: {brightness_factor}')
        if self.original_img is not None:
            self.original_img = np.clip(self.original_img + brightness_factor, 30, 240).astype(np.uint8)
            # Display Image only
            self.img = self.qimage_from_numpy(self.original_img)
            self.display_image(self.label)
        # Update the QPixmap

    def change_contrast(self, contrast_factor):
        
        logging.debug(f'Contrast Factor: {contrast_factor}')
        if self.original_img is not None:
            # Change the contrast of the image
            self.original_img = np.clip(self.original_img * contrast_factor, 30, 240).astype(np.uint8)
            self.original_img = ((self.original_img - self.original_img.min()) / (self.original_img.max() - self.original_img.min()) * 255).astype(np.uint8) 
            # Display Image only
            self.img = self.qimage_from_numpy(self.original_img)
            self.display_image(self.label)
        # Update the QPixmap

    def qimage_from_numpy(self, numpy_array):
        height, width = numpy_array.shape
        bytes_per_line = width
        q_image = QImage(numpy_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap.fromImage(q_image)
    
    def region_update(self):
        if self.id == 0:
            for img in Image.image_instances:
                if img.id is not self.id:
                    img.sync_roi_position(self.ft_roi)
                
        self.inner_img, self.outer_img =  self.return_region_slice()
        if self.checkbox.isChecked():
            new_img_fft = self.outer_img
        else:
            new_img_fft = self.inner_img
        
        print("Awl Mara", new_img_fft)
        print("check state:", self.checkbox.isChecked())
        # # Perform the inverse Fourier transform
        new_img = np.fft.ifft2(np.fft.ifftshift(new_img_fft))
        self.untouch = new_img
        self.original_img = new_img
        self.analyze_frequency_content()
              
    # Returns the area of data inside and outside the mask created by the ROI
    def return_region_slice(self):
        data = self.fft_shift
                
        # Get index ranges of data from ROI
        data_slice_indices, QTrans = self.ft_roi.getArraySlice(data, self.image_item, returnSlice=True)
        logging.debug("Sliced indices: %s", data_slice_indices)
        
        # Setup a mask the size of ROI
        mask = np.full(data.shape, False)
        logging.debug("Number of ones in mask before slicing: %d", np.count_nonzero(mask))
        mask[data_slice_indices] = True
        logging.debug("Number of ones in mask after slicing: %d and its shape: %s", np.count_nonzero(mask), mask.shape)
        masked_data_in = data * mask
        logging.debug("Masked in: %s", str(masked_data_in[0][:5]))
        logging.debug("Masked in shape: %s", masked_data_in.shape)
        masked_data_out = data.copy()
        masked_data_out[mask] = 0
        logging.debug("Masked out: %s", str(masked_data_out[0][:5]))
        logging.debug("Masked out shape: %s", masked_data_out.shape)

        
        return (masked_data_in, masked_data_out)
    
    def add_scale_handles_ROI(self):
        positions = np.array([[0,0], [1,0], [1,1], [0,1]])
        for pos in positions:        
            self.ft_roi.addScaleHandle(pos = pos, center = 1 - pos)
              
#Resetting
    def center_ROI_to_image(self):
        roi_rect = self.ft_roi.size()
        half_width = roi_rect[0] / 2
        half_height = roi_rect[1] / 2
        center = self.image_item.boundingRect().center()
        adjusted_center = [center.x() - 2*half_width, center.y()- 4*half_height]
        self.ft_roi.setPos(adjusted_center)
            
    def set_ROI_size_to_image(self):
        self.ft_roi.setSize(size = (self.image_item.boundingRect().width(), self.image_item.boundingRect().height()))
               
    def reset_ROI(self):
        self.center_ROI_to_image()
 