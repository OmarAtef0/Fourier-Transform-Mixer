import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QMouseEvent
from task4 import Ui_MainWindow
from image import Image
from mixer import Mixer

'''WHATS NEEDED:
1-Fix the reshape image function
2-Add contrast to all images "It works on first image only"
3-Add the rectangle feature to take a part of image
4- Refactoring to add functions to new class instead of Main class 
'''
class FourierTransformMixer(QMainWindow):
  
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  
    
    self.speed_sliders= [self.ui.speed_slider,self.ui.speed_slider_2,self.ui.speed_slider_3,self.ui.speed_slider_4]
    self.combos_input = [self.ui.comboBox, self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4]
    self.combos_output = [self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9]
    self.labels = [self.ui.label_1, self.ui.label_3, self.ui.label_5, self.ui.label_7]
    self.spectrum_labels = [self.ui.label_2, self.ui.label_4, self.ui.label_6, self.ui.label_8]
    self.output_labels = [self.ui.outputlabel, self.ui.outputlabel_2]
    # Connect LCDNumber widgets to weights
    self.lcd_numbers = [self.ui.lcdNumber, self.ui.lcdNumber_2, self.ui.lcdNumber_3, self.ui.lcdNumber_4]

     # Connect mouse events for brightness and contrast adjustment
    self.ui.label_1.mousePressEvent = self.on_mouse_press
    self.ui.label_1.mouseMoveEvent = self.on_mouse_move
    self.ui.label_1.mouseReleaseEvent = self.on_mouse_release
    self.x = None
    self.y = None
    self.mouse_pressed = False
    self.brightness_accumulated, self.contrast_accumulated = 0,0

    for i, weight_lcd in enumerate(self.lcd_numbers):
        weight_lcd.display(self.speed_sliders[i].value())

    for slider, weight_lcd in zip(self.speed_sliders, self.lcd_numbers):
        slider.valueChanged.connect(weight_lcd.display)

    self.images = [Image() for _ in range(4)]
    self.mixer  = Mixer(self.images,self.ui,self.combos_output,output_labels=self.output_labels)

    for speed_slider in self.speed_sliders:
        speed_slider.valueChanged.connect(self.set_weights)
        

    for label, spectrum_label, image in zip(self.labels, self.spectrum_labels, self.images):
        label.mouseDoubleClickEvent = lambda event, img=image, lbl1=label, lbl2=spectrum_label: img.browse_file(lbl1, lbl2)

    for combo, spectrum_label, image in zip(self.combos_input, self.spectrum_labels, self.images):
      combo.currentIndexChanged.connect(lambda index, img=image ,cb=combo,spct_lbl=spectrum_label: self.handle_combobox_change(index, img,cb,spct_lbl))


    self.ui.modeCombo.currentIndexChanged.connect(self.update_combobox_options)
    self.ui.mixButton.clicked.connect(self.mixer.mix_images)


  def handle_combobox_change(self, index,image,combo,spct_lbl ):
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
        weights = [slider.value() for slider in self.speed_sliders]
        self.mixer.set_weights(weights)

  def on_mouse_press(self, event: QMouseEvent):
    if (
        event.button() == Qt.MouseButton.LeftButton
        and self.ui.label_1.geometry().contains(event.pos())
    ):
        self.mouse_pressed = True
        self.initial_pos = event.pos()


  def on_mouse_move(self, event: QMouseEvent):
    if self.mouse_pressed:
        self.track_mouse_position(event)

        # Adjust brightness based on horizontal movement
        brightness_factor = self.brightness_accumulated
        # Adjust contrast based on vertical movement
        contrast_factor = self.contrast_accumulated

        # Apply the accumulated factors to the image
        self.images[0].change_brightness(brightness_factor)
        self.images[0].change_contrast(1.0 + contrast_factor)

        # Reset accumulated factors
        self.brightness_accumulated = 0.0
        self.contrast_accumulated = 0.0


  def on_mouse_release(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_pressed = False

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

            if abs(dx) > margin :
                # Adjust brightness based on horizontal movement
                brightness_factor = dx / 50.0
                self.brightness_accumulated += brightness_factor
                self.x = crrX
            if abs(dy) > margin:
                # Adjust contrast based on vertical movement
                contrast_factor = dy / 50.0
                self.contrast_accumulated += contrast_factor
                self.y = crrY
            
            

    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
