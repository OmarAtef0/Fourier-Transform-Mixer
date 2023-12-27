import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import  QMessageBox
import logging

logging.basicConfig(filename = 'debugging.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', filemode='w')

class Mixer():
    def __init__(self, images,ui,combo_output,output_labels):
        self.images = images
        self.weights = []
        self.ui = ui
        self.combos_output = combo_output
        self.output_labels = output_labels

    def set_weights(self, component_weights):
        self.weights = component_weights

    def mix_images(self):
        if not self.weights:
            QMessageBox.critical(None, "Error", "No weights provided.")
            return None

        # Create a list to store weighted components
        if self.ui.modeCombo.currentText() == "Mag/Phase":
            magnitude = np.zeros(self.images[0].shape)
            phase = np.zeros(self.images[0].shape)

            for i,(img, weight, combo) in enumerate(zip(self.images, self.weights, self.combos_output)):
                selected_component = combo.currentText()

                if selected_component == "Magnitude":
                    magnitude += (weight / 100) * img.mag_shifted
                    logging.debug(f'Mag after component {i} equal to: %s', str(magnitude[0][:5]))
                elif selected_component == "Phase":

                    phase += (weight / 100) * img.phase_shifted
                    logging.debug(f'phase after component {i} using the weight {weight} equal to: %s', str(phase[0][:5]))


            # Combine magnitude and phase components
            mixed_image = np.real(np.fft.ifft2(np.fft.ifftshift(magnitude * np.exp(1j * phase))))
            logging.debug(f'Original image: %s', str(self.images[0].original_img[0][:7]))
            logging.debug("Mixed Image before clipping: %s", str(mixed_image[0][:7]))
            mixed_image = np.clip(mixed_image, 0, 255)
            logging.debug("After clipping: %s", str(mixed_image[0][:7]))

            

        elif self.ui.modeCombo.currentText() == "Real/Imag":
            real = np.zeros(self.images[0].shape)
            imag = np.zeros(self.images[0].shape)

            for img, weight, combo in zip(self.images, self.weights, self.combos_output):
                selected_component = combo.currentText()

                if selected_component == "Real":
                    real += (weight / 100) * img.real_shifted
                elif selected_component == "Imaginary":
                    imag += (weight / 100) * img.imag_shifted
            
            
            mixed_image = np.abs(np.fft.ifft2(real + imag * 1j))
            logging.debug("Before clipping: %s", mixed_image)
            mixed_image= np.clip(mixed_image, 0,255).astype(np.uint8)
            logging.debug("after clipping: %s",mixed_image)
        output_label = self.output_labels
        output_label_combo = self.ui.outputBox 
        self.display_mixed(mixed_image,output_label,output_label_combo)

    def display_mixed(self,mixed_image,output_label,output_label_combo):
        
        mixed_image = cv2.normalize(mixed_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        mixed_image= cv2.resize(mixed_image,(350,300))
        logging.debug("Mixed Image After Normalaizing: %s", mixed_image)
        height, width = mixed_image.shape
        bytes_per_line = width
        mixed_image_bytes = mixed_image.tobytes()
        q_image = QImage(mixed_image_bytes, width, height, bytes_per_line, QImage.Format_Grayscale8)
    
        if output_label_combo.currentText() == "Output 1":
            pixmap = QPixmap.fromImage(q_image)
            output_label[0].setPixmap(pixmap)
            output_label[0].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            
        elif output_label_combo.currentText() == "Output 2":
            pixmap = QPixmap.fromImage(q_image)
            output_label[1].setPixmap(pixmap)
            output_label[1].setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        #Matplotlib integerating bs morhaq
            # self.fig, self.ax = plt.subplots()
            # self.canvas = FigureCanvas(self.fig)
            # self.ui.canvasholder.addWidget(self.canvas)
            # ax = self.canvas.figure.add_subplot(111)
            # ax.imshow(mixed_image, cmap='gray')
            # self.canvas.draw()


