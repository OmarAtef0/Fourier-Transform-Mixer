import cv2
import numpy as np
from PyQt5.QtGui import QImageReader,QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel

class Image():
    id_counter = 0
    def __init__(self):
        self.id = Image.id_counter
        Image.id_counter += 1
        self.file_path = None
        self.name = None
        self.shape = None
        self.fft = None
        self.fft_shift = None
        self.fft_phase = None
        self.fft_mag = None
        self.fft_real = None
        self.fft_imag = None

    def get_id(self):
        return self.id
    
    def browse_file(self, label):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(None, "Browse Image File", "", "Images (*.png *.jpg *.bmp *.gif *.tif *.tiff);;All Files (*)", options=options)
        if path:
            self.set_file_path(path, label)
    
    def set_file_path(self, path,label):
        self.path = path
        self.load_image(path,label)

    def load_image(self, path,label, show=True):
        try:
            # Read and convert the image
            self.img = cv2.imread(path).astype(np.float32)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self.shape = self.img.shape

            # Convert to QImage
            bytes_per_line = 1 * self.shape[0]
            q_image = QImage(self.img.data, self.shape[0], self.shape[1], bytes_per_line, QImage.Format_Grayscale8)

            # Set the original and current images as QPixmap
            self.img = QPixmap.fromImage(q_image)

            if show:
                # Display the image using a PyQt widget (e.g., QLabel)
                self.display_image(label)
        except cv2.error as e:
            print(f"Error: Couldn't load the image at {path}. OpenCV error: {str(e)}")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}")

    def display_image(self,label):
        # add the label where image is going to be displayed
        self.label = label
        label.setPixmap(self.img)

       

