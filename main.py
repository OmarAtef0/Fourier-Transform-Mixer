import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from task4 import Ui_MainWindow
from image import Image

class FourierTransformMixer(QMainWindow):
  
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  
    
    self.images = [Image() for _ in range(4)]
    self.addbuttons = [self.ui.addButton,self.ui.addButton_2,self.ui.addButton_3,self.ui.addButton_4 ]
    labels = [self.ui.label_1, self.ui.label_3, self.ui.label_5, self.ui.label_7]
    spectrum_labels = [self.ui.label_2, self.ui.label_4, self.ui.label_6, self.ui.label_8]
    combos = [self.ui.comboBox, self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4]


    for label, spectrum_label, image in zip(labels, spectrum_labels, self.images):
        label.mouseDoubleClickEvent = lambda event, img=image, lbl1=label, lbl2=spectrum_label: img.browse_file(lbl1, lbl2)

    for combo, spectrum_label, image in zip(combos, spectrum_labels, self.images):
      combo.currentIndexChanged.connect(lambda index, img=image ,cb=combo,spct_lbl=spectrum_label: self.handle_combobox_change(index, img,cb,spct_lbl))

    for button in self.addbuttons:
            button.clicked.connect(self.update_combobox_options)


  def handle_combobox_change(self, index,image,combo,spct_lbl ):
    try:
        spectrum_type = combo.currentText()
        image.plot_spectrum(spectrum_type,spct_lbl)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # self.ui.comboBox.currentIndexChanged.connect(self.handle_combobox_change)

    # def handle_combobox_change(self, index):
    #     try:
    #         spectrum_type = self.ui.comboBox.currentText()
    #         self.images[0].plot_spectrum(spectrum_type)
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")

    # self.ui.label_1.mouseDoubleClickEvent = lambda event: self.image_1.browse_file(self.ui.label_1,self.ui.label_2)
    # self.ui.label_3.mouseDoubleClickEvent = lambda event: self.image_3.browse_file(self.ui.label_3,self.ui.label_4)
    # self.ui.label_5.mouseDoubleClickEvent = lambda event: self.image_5.browse_file(self.ui.label_5,self.ui.label_6)
    # self.ui.label_7.mouseDoubleClickEvent = lambda event: self.image_7.browse_file(self.ui.label_7,self.ui.label_8)


    # self.ui.comboBox_2.currentIndexChanged.connect(lambda index: self.image_3.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_4))
    # self.ui.comboBox_3.currentIndexChanged.connect(lambda index: self.image_5.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_6))
    # self.ui.comboBox_4.currentIndexChanged.connect(lambda index: self.image_7.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_8))
    # self.ui.comboBox.currentIndexChanged.connect(  lambda index: self.handle_combobox_change(self.ui.label_2))

  def update_combobox_options(self):
      # Identify the clicked button
      clicked_button = self.sender()

      # Get the selected option from the clicked button's corresponding combobox
      selected_option = None
      combo_to_exclude = None

      if clicked_button == self.ui.addButton:
          selected_option = self.ui.comboBox_6.currentText()
          combo_to_exclude = self.ui.comboBox_6
      elif clicked_button == self.ui.addButton_2:
          selected_option = self.ui.comboBox_7.currentText()
          combo_to_exclude = self.ui.comboBox_7
      elif clicked_button == self.ui.addButton_3:
          selected_option = self.ui.comboBox_8.currentText()
          combo_to_exclude = self.ui.comboBox_8
      elif clicked_button == self.ui.addButton_4:
          selected_option = self.ui.comboBox_9.currentText()
          combo_to_exclude = self.ui.comboBox_9

      # Define the possible options for each selection
      options_mapping = {
          "----": ["----", "Magnitude", "Phase", "Real", "Imaginary"],
          "Magnitude": ["----","Magnitude", "Phase"],
          "Phase": ["----","Magnitude", "Phase"],
          "Real": ["----","Real", "Imaginary"],
          "Imaginary": ["=---","Real", "Imaginary"]
      }

      # Update options in comboboxes, excluding the one corresponding to the clicked button
      for combo in [self.ui.comboBox_6, self.ui.comboBox_7, self.ui.comboBox_8, self.ui.comboBox_9]:
          if combo != combo_to_exclude:
              combo.clear()
              options = options_mapping[selected_option]
              combo.addItems(options)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
