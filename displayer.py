import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QMouseEvent
from task4 import Ui_MainWindow
from image import Image
from mixer import Mixer
import logging

logging.basicConfig(filename = 'debug.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', filemode='w')

class ImageDisplayer():
  
  def __init__(self, label, spectrum_label):
        self.label = label
        self.spectrum_label = spectrum_label
        self.image = None
        self.brightness_accumulated = 0.0
        self.contrast_accumulated = 0.0
        self.x = None
        self.y = None
        self.mouse_pressed = False

  def handle_combobox_change(self,image,combo,spct_lbl ):
    try:
        spectrum_type = combo.currentText()
        image.plot_spectrum(spectrum_type,spct_lbl)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


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

                # Reset accumulated factors for the current image
                self.brightness_accumulated[i] = 0.0
                self.contrast_accumulated[i] = 0.0


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
                    brightness_factor = dx / 50.0
                    self.brightness_accumulated[i] += brightness_factor

                if abs(dy) > margin:
                    # Adjust contrast based on vertical movement
                    contrast_factor = dy / 50.0
                    self.contrast_accumulated[i] += contrast_factor

            self.x = crrX
            self.y = crrY

            
            

    

