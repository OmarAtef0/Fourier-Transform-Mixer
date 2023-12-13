import numpy as np
import cv2
from PyQt5.QtGui import QImage, QPixmap

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
            print("Error: No weights provided.")
            return None

        # Create a list to store weighted components
        if self.ui.modeCombo.currentText() == "Mag/Phase":
            magnitude = np.zeros(self.images[0].shape)
            phase = np.zeros(self.images[0].shape)

            for img, weight, combo in zip(self.images, self.weights, self.combos_output):
                selected_component = combo.currentText()

                if selected_component == "Magnitude":
                    print("MAG SHIFTED:",img.fft_components[0])
                    magnitude += (weight / 100) * img.fft_components[0]
                elif selected_component == "Phase":
                    print("Phase SHIFTED:",img.fft_components[1])
                    phase += (weight / 100) * img.fft_components[1]

                print("Selected component:", selected_component)
                print("Weights:", weight)
            mixed_image = np.abs(np.fft.ifft2(magnitude * np.exp(1j * phase)))
            print("before clipping:",mixed_image)
            mixed_image=np.clip(mixed_image, 0,225) 
            print("after clipping:",mixed_image)
            

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
            mixed_image= np.clip(mixed_image, 0,225)
            print("after clipping:",mixed_image)
        output_label = self.output_labels
        output_label_combo = self.ui.outputBox 
        self.display_mixed(mixed_image,output_label,output_label_combo)

    def display_mixed(self,mixed_image,output_label,output_label_combo):

        height, width = mixed_image.shape
        bytes_per_line = width
        mixed_image_normal =cv2.normalize(mixed_image, None, 0, 255, cv2.NORM_MINMAX)
        mixed_image_bytes = mixed_image_normal.tobytes()
        q_image = QImage(mixed_image_bytes, width, height, bytes_per_line, QImage.Format_Grayscale8)
        if output_label_combo.currentText() == "Output 1":
            pixmap = QPixmap.fromImage(q_image)
            output_label[0].setPixmap(pixmap)

        elif output_label_combo.currentText() == "Output 2":
            pixmap = QPixmap.fromImage(q_image)
            output_label[1].setPixmap(pixmap)



