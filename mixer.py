import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import  QMessageBox

class Mixer:
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
                    print("MAG SHIFTED:",img.fft_components[0][0][:5])
                    magnitude += (weight / 100) * img.mag_shifted
                    print(f'Mag after component {i} equal to: {magnitude[0][:5]}')
                elif selected_component == "Phase":
                    print("Phase SHIFTED:",img.fft_components[1][0][:5]) 
                    phase += (weight / 100) * img.fft_components[1]
                    print(f'phase after component {i} using the weight {weight} equal to: {phase[0][:5]}')


            # Combine magnitude and phase components
            mixed_image = np.abs(np.real(np.fft.ifft2(magnitude * np.exp(1j * phase)))) 
            print(f'Original image: {self.images[0].original_img[0][:10]}')
            print("Mixed Image before clipping:",mixed_image[0][:10])
            mixed_image=np.clip(mixed_image, 0,255) 
            print("after clipping:",mixed_image[0][:10])
            

        elif self.ui.modeCombo.currentText() == "Real/Imag":
            real = np.zeros(self.images[0].shape)
            imag = np.zeros(self.images[0].shape)

            for img, weight, combo in zip(self.images, self.weights, self.combos_output):
                selected_component = combo.currentText()

                if selected_component == "Real":
                    real += (weight / 100) * img.fft_components[2]
                elif selected_component == "Imaginary":
                    imag += (weight / 100) * img.fft_components[3]
            
            
            mixed_image = np.abs(np.fft.ifft2(real + imag * 1j))
            print ("before cliping:",mixed_image)
            mixed_image= np.clip(mixed_image, 0,255).astype(np.uint8)
            print("after clipping:",mixed_image)
        output_label = self.output_labels
        output_label_combo = self.ui.outputBox 
        self.display_mixed(mixed_image,output_label,output_label_combo)

    def display_mixed(self,mixed_image,output_label,output_label_combo):
        
        mixed_image = cv2.normalize(mixed_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        print("Mixed Image After Normalaizing:",mixed_image)
        height, width = mixed_image.shape
        bytes_per_line = width
        mixed_image_bytes = mixed_image.tobytes()
        q_image = QImage(mixed_image_bytes, width, height, bytes_per_line, QImage.Format_Grayscale8)
    
        if output_label_combo.currentText() == "Output 1":
            pixmap = QPixmap.fromImage(q_image)
            output_label[0].setPixmap(pixmap)

            
        elif output_label_combo.currentText() == "Output 2":
            pixmap = QPixmap.fromImage(q_image)
            output_label[1].setPixmap(pixmap)

        #Matplotlib integerating bs morhaq
            # self.fig, self.ax = plt.subplots()
            # self.canvas = FigureCanvas(self.fig)
            # self.ui.canvasholder.addWidget(self.canvas)
            # ax = self.canvas.figure.add_subplot(111)
            # ax.imshow(mixed_image, cmap='gray')
            # self.canvas.draw()


