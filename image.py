import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtGui import QImageReader, QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5 import QtCore

class Image():
    #Global Variables
    image_instances = []
    max_width = 350
    max_height = 250
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
        self.fft, self.fft_shift = None, None
        self.phase, self.phase_shifted = None, None
        self.mag, self.mag_shifted = None, None
        self.real, self.real_shifted= None, None
        self.imag, self.imag_shifted = None, None
        Image.image_instances.append(self)

    def get_id(self):
        return self.id

    def browse_file(self, label, spectrum_label):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(None, "Browse Image File", "", "Images (*.png *.jpg *.bmp *.gif *.tif *.tiff);;All Files (*)", options=options)
        if path:
            self.spectrum_label = spectrum_label
            self.set_file_path(path, label)

    def set_file_path(self, path, label):
        self.path = path
        self.load_image(path, label)

    def load_image(self, path, label,show=True):
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
        self.original_img = self.original_img.astype(np.uint8)
        cv2.normalize(self.original_img, self.original_img, 0, 255, cv2.NORM_MINMAX)
        
        # Set the original and current images as QPixmap
        self.img = self.qimage_from_numpy(self.original_img)
        
        # Check if the image is not None
        if self.img is not None:
            # Set the pixmap only if the image is not None
            label.setPixmap(self.img)
            label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    #WE CAN DELETE THIS FUNCTION
    def reshape(self, img_height, img_width):
        """
        Resize the image to the specified dimensions.

        Parameters:
        - img_height (int): The current height of the image.
        - img_width (int): The current width of the image.

        Returns:
        - None
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

        Parameters:
        - cls (class): The class reference.

        Returns:
        - None
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
                    img.compute_fourier_transform(img.spectrum_label)
            except Exception as e:
                print(f"Error in instance {img.get_id()}: {str(e)}")

    def compute_fourier_transform(self, spectrum_label, show=True):
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
            print(f"The type is {spectrum_type} and its values are: {spectrum[0][:5]} , its shape is: {spectrum.shape}")

            # Check for NaN values
            if np.isnan(spectrum).any():
                print(f"Error: Spectrum type '{spectrum_type}' contains NaN values.")
                spectrum = np.zeros_like(spectrum)  # Set to black image in case of NaN values

            # Normalize the spectrum values to be between 0 and 255

            # spectrum_normalized = cv2.normalize(spectrum, None, 0, 255, cv2.NORM_MINMAX) 
            spectrum_normalized = ((spectrum - spectrum.min()) / (spectrum.max() - spectrum.min()) * 255).astype(np.uint8) 

            # Convert to bytes using NumPy functions
            spectrum_bytes = spectrum_normalized.tobytes()

            # Convert to QImage
            q_image = QImage(spectrum_bytes, spectrum.shape[1], spectrum.shape[0], spectrum.shape[1], QImage.Format_Grayscale8)

            # Set the image in the QLabel
            spectrum_label.setPixmap(QPixmap.fromImage(q_image))
            spectrum_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        else:
            print(f"Error: Spectrum type '{spectrum_type}' not found in the dictionary.")


    def change_brightness(self, brightness_factor):
          
        # Change the brightness of the image
        print(f'Brightness Factor: {brightness_factor}')
        if self.original_img is not None:
            self.original_img = np.clip(self.original_img + brightness_factor, 0, 255).astype(np.uint8)
            # Update Fourier Transform components and display
            self.compute_fourier_transform(self.spectrum_label)
            self.img = self.qimage_from_numpy(self.original_img)
            self.display_image(self.label)
        # Update the QPixmap

    def change_contrast(self, contrast_factor):

        
        print(f'Contrast Factor: {contrast_factor}')
        if self.original_img is not None:
            # Change the contrast of the image
            self.original_img = np.clip(self.original_img * contrast_factor, 0, 255).astype(np.uint8)
            # Update Fourier Transform components and display
            self.compute_fourier_transform(self.spectrum_label)
            self.img = self.qimage_from_numpy(self.original_img)
            self.display_image(self.label)
        # Update the QPixmap

    def qimage_from_numpy(self, numpy_array):
        height, width = numpy_array.shape
        bytes_per_line = width
        q_image = QImage(numpy_array.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        return QPixmap.fromImage(q_image)
    





[
    {
        "id": "777e21d8fb7005c6",
        "type": "json",
        "z": "88da2bec208da9fc",
        "name": "",
        "property": "payload",
        "action": "",
        "pretty": false,
        "x": 190,
        "y": 140,
        "wires": [
            [
                "9f828d0c941740ff"
            ]
        ]
    },
    {
        "id": "9f828d0c941740ff",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "var value = JSON.parse(JSON.stringify(msg.payload));\nmsg.payload = value;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 320,
        "y": 220,
        "wires": [
            [
                "fe6fc76d0b7ed705",
                "3aea9c82799acd44",
                "edf7c2341a1b106b"
            ]
        ]
    },
    {
        "id": "fe6fc76d0b7ed705",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload = msg.payload.flowRate;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 140,
        "wires": [
            [
                "1ada5da722d25cc3"
            ]
        ]
    },
    {
        "id": "edf7c2341a1b106b",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload = msg.payload.temperatureCelsius;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 300,
        "wires": [
            [
                "a8b9a012f0bcd88a"
            ]
        ]
    },
    {
        "id": "3aea9c82799acd44",
        "type": "function",
        "z": "88da2bec208da9fc",
        "name": "",
        "func": "msg.payload = msg.payload.totalMilliLiters;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 500,
        "y": 220,
        "wires": [
            [
                "94261317f1debd03"
            ]
        ]
    },
    {
        "id": "94261317f1debd03",
        "type": "ui_chart",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 8,
        "width": 15,
        "height": 4,
        "label": "Flow Rate",
        "chartType": "line",
        "legend": "false",
        "xformat": "HH:mm:ss",
        "interpolate": "linear",
        "nodata": "",
        "dot": false,
        "ymin": "",
        "ymax": "",
        "removeOlder": 1,
        "removeOlderPoints": "",
        "removeOlderUnit": "3600",
        "cutout": 0,
        "useOneColor": false,
        "useUTC": false,
        "colors": [
            "#1f77b4",
            "#aec7e8",
            "#ff7f0e",
            "#2ca02c",
            "#98df8a",
            "#d62728",
            "#ff9896",
            "#9467bd",
            "#c5b0d5"
        ],
        "outputs": 1,
        "useDifferentColor": false,
        "className": "",
        "x": 690,
        "y": 220,
        "wires": [
            []
        ]
    },
    {
        "id": "a8b9a012f0bcd88a",
        "type": "ui_gauge",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 1,
        "width": 8,
        "height": 4,
        "gtype": "wave",
        "title": "Temperature",
        "label": "°C",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 700,
        "y": 300,
        "wires": []
    },
    {
        "id": "1ada5da722d25cc3",
        "type": "ui_gauge",
        "z": "88da2bec208da9fc",
        "name": "",
        "group": "218fb04944bee58f",
        "order": 3,
        "width": 9,
        "height": 4,
        "gtype": "gage",
        "title": "Total Milliliters",
        "label": "mL",
        "format": "{{value}}",
        "min": 0,
        "max": "1023",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "className": "",
        "x": 700,
        "y": 140,
        "wires": []
    },
    {
        "id": "46a301b8aa20f403",
        "type": "serial in",
        "z": "88da2bec208da9fc",
        "name": "",
        "serial": "632ce51bae434d89",
        "x": 90,
        "y": 240,
        "wires": [
            [
                "777e21d8fb7005c6"
            ]
        ]
    },
    {
        "id": "218fb04944bee58f",
        "type": "ui_group",
        "name": "Hemodylasis Parameters Visuilization",
        "tab": "b10389acabce7f3b",
        "order": 1,
        "disp": true,
        "width": "20",
        "collapse": false,
        "className": ""
    },
    {
        "id": "632ce51bae434d89",
        "type": "serial-port",
        "serialport": "COM6",
        "serialbaud": "9600",
        "databits": "8",
        "parity": "none",
        "stopbits": "1",
        "waitfor": "",
        "dtr": "none",
        "rts": "none",
        "cts": "none",
        "dsr": "none",
        "newline": "\\n",
        "bin": "false",
        "out": "char",
        "addchar": "",
        "responsetimeout": "10000"
    },
    {
        "id": "b10389acabce7f3b",
        "type": "ui_tab",
        "name": "Dialysis Parameters Visualization",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    }
]
