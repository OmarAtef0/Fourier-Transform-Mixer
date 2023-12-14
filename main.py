import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from task4 import Ui_MainWindow
from image import Image
from mixer import Mixer


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
    
if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
