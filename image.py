import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImageReader, QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel

class Image():
    #Global Variables
    image_instances = []
    initial_width = 320
    initial_height = 200
    ID =0
    def __init__(self):
        self.id = Image.ID
        Image.ID +=1
        self.path = None
        self.original_img = None  # Store the original image data (NumPy array)
        self.img = None  # for display only
        # self.displayed_after_reshape = False  # Flag to track if displayed after reshape
        self.label = None  # QLabel containing Image
        self.spectrum_label = None # QLabel Containing the Spectrums
        self.shape = None

        #Image Components
        self.fft ,self.fft_shift = None ,None
        self.phase , self.phase_shifted = None,None
        self.mag ,self.mag_shifted = None, None
        self.real, self.real_shifted= None, None
        self.imag, self.imag_shifted = None, None
        Image.image_instances.append(self)

    def get_id(self):
        return self.id

    def browse_file(self, label,spectrum_label):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(None, "Browse Image File", "", "Images (*.png *.jpg *.bmp *.gif *.tif *.tiff);;All Files (*)", options=options)
        if path:
            self.spectrum_label = spectrum_label
            self.set_file_path(path, label)

    def set_file_path(self, path, label):
        self.path = path
        self.load_image(path, label)

    def load_image(self, path, label ,show=True):
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
            bytes_per_line = 1 * self.shape[1]
            q_image = QImage(self.original_img.data, self.shape[1], self.shape[0], bytes_per_line, QImage.Format_Grayscale8)

            # Set the original and current images as QPixmap
            self.img = QPixmap.fromImage(q_image)
            self.compute_fourier_transform(self.spectrum_label)
            if show: #used for hide/show
                # Display the image using a PyQt widget (e.g., QLabel)
                self.display_image(label)
        except cv2.error as e:
            print(f"Error: Couldn't load the image at {path}. OpenCV error: {str(e)}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")

    def display_image(self, label):
        """
        Display the image on the specified QLabel.

        Parameters:
        - label (QLabel): The QLabel where the image is going to be displayed.

        Returns:
        - None
        """
        # Check if the image is not None
        if self.img is not None:
            # Set the pixmap only if the image is not None
            label.setPixmap(self.img)


    def reshape(self, img_height, img_width):
        """
        Resize the image to the specified dimensions.

        Parameters:
        - img_height (int): The current height of the image.
        - img_width (int): The current width of the image.

        Returns:
        - None
        """
        new_height = min(Image.initial_height, img_height)
        new_width = min(Image.initial_width, img_width)
        Image.initial_height = new_height
        Image.initial_width = new_width

        # Resize the image
        self.original_img = cv2.resize(self.original_img, (new_width, new_height))
        # Update the shape attribute
        self.shape = self.original_img.shape


    @classmethod
    def reshape_all(cls):
        """
        Resize all images in a list of Image instances to the smallest dimensions among them.

        Parameters:
        - cls (class): The class reference.

        Returns:
        - None
        """
        # Find the smallest image dimensions among all instances
        min_height = min(inst.original_img.shape[0] for inst in cls.image_instances if inst.original_img is not None)
        min_width = min(inst.original_img.shape[1] for inst in cls.image_instances if inst.original_img is not None)

        # Resize all images to the smallest dimensions
        for inst in cls.image_instances:
            try:
                if inst.original_img is not None:
                    inst.reshape(min_height, min_width)
                    inst.display_image(inst.label)
            except Exception as e:
                print(f"Error in instance {inst.get_id()}: {str(e)}")

    def compute_fourier_transform(self,spectrum_label, show=True):
        """
        Compute the 2D Fourier Transform and related components of the image.

        Parameters:
        - show (bool, optional): If True, display visualizations of the Fourier Transform components.
                                Default is True.

        Returns:
        - None
        """
        # Compute the 2D Fourier Transform
        self.fft = np.fft.fft2(self.original_img)

        # Shift the zero-frequency component to the center
        self.fft_shift = np.fft.fftshift(self.fft)

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
        self.fft_components= [np.multiply(np.log(self.mag_shifted+1),20) 
                             , self.phase_shifted
                            , self.real_shifted ,
                              self.imag_shifted]

        #contruct a dictionary to map each component to its type
        self.fft_dict = {
                        "FT Magnitude": self.fft_components[0],
                        "FT Phase": self.fft_components[1],
                        "FT Real": self.fft_components[2],
                        "FT Imaginary": self.fft_components[3] }


        if show: 
            # Plot the magnitude spectrum by default
            self.plot_spectrum("FT Magnitude", spectrum_label) 

    def plot_spectrum(self, spectrum_type, spectrum_label):
        """
        Plot the selected spectrum type.

        Parameters:
        - spectrum_type (str): The type of spectrum to plot.

        Returns:
        - None
        """
        if spectrum_type in self.fft_dict:
            # Retrieve the corresponding spectrum from the dictionary
            spectrum = self.fft_dict[spectrum_type]
            print(f"The type is {spectrum_type} and its values are: {spectrum[0][:10]} ,its shape is: {spectrum.shape}")

            # Check for NaN values
            if np.isnan(spectrum).any():
                print(f"Error: Spectrum type '{spectrum_type}' contains NaN values.")
                spectrum = np.zeros_like(spectrum)  # Set to black image in case of NaN values

            # Normalize the spectrum values to be between 0 and 255

            # spectrum_normalized = cv2.normalize(spectrum , None,0 , 255,cv2.NORM_MINMAX) ---> Same approach,Same result
            spectrum_normalized = ((spectrum - spectrum.min()) / (spectrum.max() - spectrum.min()) * 255).astype(np.uint8)

            # Convert to bytes using NumPy functions
            spectrum_bytes = spectrum_normalized.tobytes()

            # Convert to QImage
            q_image = QImage(spectrum_bytes, spectrum.shape[1], spectrum.shape[0], spectrum.shape[1], QImage.Format_Grayscale8)

            # Set the image in the QLabel
            spectrum_label.setPixmap(QPixmap.fromImage(q_image))
        else:
            print(f"Error: Spectrum type '{spectrum_type}' not found in the dictionary.")
