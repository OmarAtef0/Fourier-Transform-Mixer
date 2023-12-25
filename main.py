import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QIcon, QMouseEvent
from task4 import Ui_MainWindow
from image import Image
from mixer import Mixer
import qdarkstyle
import pyqtgraph as pg
import logging

logging.basicConfig(filename = 'debugging.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', filemode='w')

'''
What's Left:
'''
class FourierTransformMixer(QMainWindow):
  
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  
    
    self.weight_sliders= [self.ui.weight_slider, self.ui.weight_slider_2, self.ui.weight_slider_3, self.ui.weight_slider_4]
    self.combos_input = [self.ui.comboBox, self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4]
    self.combos_output = [self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9]
    self.labels = [self.ui.label_1, self.ui.label_3, self.ui.label_5, self.ui.label_7]
    self.spectrums = [self.ui.spectrum_1, self.ui.spectrum_2, self.ui.spectrum_3, self.ui.spectrum_4]
    self.output_labels = [self.ui.outputlabel, self.ui.outputlabel_2]
    self.check_boxes = [self.ui.checkBox,self.ui.checkBox_2,self.ui.checkBox_3,self.ui.checkBox_4]
    # Connect LCDNumber widgets to weights
    self.lcd_numbers = [self.ui.lcdNumber, self.ui.lcdNumber_2, self.ui.lcdNumber_3, self.ui.lcdNumber_4]
    self.images = [Image() for _ in range(4)]
    self.mixer  = Mixer(self.images, self.ui, self.combos_output, output_labels=self.output_labels)
    self.brightness_accumulated = {i: 0.0 for i in range(len(self.images))}
    self.contrast_accumulated = {i: 0.0 for i in range(len(self.images))}
    # Connect mouse events for brightness and contrast adjustment
    
    self.x = None
    self.y = None
    self.mouse_pressed = False
    self.initial_roi_position = None
    self.ROI_Maxbounds = QRectF(0, 0, 100, 100)

    self.ui.modeCombo.currentIndexChanged.connect(self.update_combobox_options)
    
    for label in self.labels:
        label.mousePressEvent = self.on_mouse_press
        label.mouseMoveEvent = self.on_mouse_move
        label.mouseReleaseEvent = self.on_mouse_release
     
    for i, weight_lcd in enumerate(self.lcd_numbers):
        weight_lcd.display(self.weight_sliders[i].value())

    for slider, weight_lcd in zip(self.weight_sliders, self.lcd_numbers):
        slider.valueChanged.connect(weight_lcd.display)

    for weight_slider in self.weight_sliders:
        weight_slider.valueChanged.connect(self.set_weights)
        weight_slider.valueChanged.connect(self.mixer.mix_images)
        
    for label, spectrum, image,checkbox in zip(self.labels, self.spectrums, self.images,self.check_boxes):
        label.mouseDoubleClickEvent = lambda event, img=image, lbl1=label, lbl2=spectrum, chckbx=checkbox: img.browse_file(lbl1, lbl2,chckbx)
        
    for checkbox, image in zip(self.check_boxes, self.images):
            image.connect_checkbox(checkbox)

  def handle_combobox_change(self, index, image, combo):
    try:
        spectrum_type = combo.currentText()
        image.plot_spectrum(spectrum_type)
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

  def update_combobox_options(self):
      # Identify the clicked button
      mode_button = self.ui.modeCombo.currentText()

      selected_option = None

      if mode_button == "Mag/Phase":
          selected_option = mode_button
      elif mode_button == "Real/Imag":
          selected_option = mode_button

      # Define the possible options for each selection
      options_mapping = {  
          "Mag/Phase": ["Magnitude", "Phase"],
          "Real/Imag": ["Real", "Imaginary"], 
        }

      # Update options in comboboxes, excluding the one corresponding to the clicked button
      for combo in [self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9]:
              combo.clear()
              options = options_mapping[selected_option]
              combo.addItems(options)
   
  def set_weights(self):
        weights = [slider.value() for slider in self.weight_sliders]
        self.mixer.set_weights(weights)

  def on_mouse_release(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_pressed = False

  def on_mouse_press(self, event: QMouseEvent):
    for index, label in enumerate(self.labels):
        if (
            event.button() == Qt.MouseButton.LeftButton
            and label.geometry().contains(event.pos())
        ):
            self.mouse_pressed = True
            self.initial_pos = event.pos()
            self.current_image_index = index
        elif (
            event.button() == Qt.MouseButton.RightButton
            and label.geometry().contains(event.pos())
        ):
            image_instance = self.images[index]
            if image_instance:
                image_instance.reset_ROI()
            self.reset_brightness_contrast(index)

  def reset_brightness_contrast(self, index):
    # Reset brightness and contrast for the specified image to its original state
    self.brightness_accumulated[index] = 0.0
    self.contrast_accumulated[index] = 0.0

    # Reload the original image
    self.images[index].load_image(self.images[index].path, self.labels[index])

    # Update Fourier Transform components and display
    self.images[index].display_image(self.labels[index])

  def on_mouse_move(self, event: QMouseEvent):
    if self.mouse_pressed:
        self.track_mouse_position(event)

        # Adjust brightness and contrast factors for all images
        for i, label in enumerate(self.labels):
            if label.underMouse():  # Check if the mouse is over the current label
                brightness_factor = self.brightness_accumulated[i]
                contrast_factor = self.contrast_accumulated[i]

                # Apply the accumulated factors to the current image
                self.images[i].change_brightness(brightness_factor)
                self.images[i].change_contrast(1.0 + contrast_factor)

  def track_mouse_position(self, event: QMouseEvent):
        # Track mouse position when clicking and holding
        crrX, crrY = event.pos().x(), event.pos().y()
        if self.x is None:
            self.x = crrX
            self.y = crrY
        else:
            # Calculate movement in x and y directions
            dx = crrX - self.x
            dy = crrY - self.y

            # Controls Sensitivity
            margin = 10

            for i in range(len(self.images)):
                if abs(dx) > margin:
                    # Adjust brightness based on horizontal movement
                    brightness_factor = dx / 100.0
                    self.brightness_accumulated[i] += brightness_factor

                if abs(dy) > margin:
                    # Adjust contrast based on vertical movement
                    contrast_factor = dy / 100.0
                    self.contrast_accumulated[i] += contrast_factor

            self.x = crrX
            self.y = crrY
          

    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
