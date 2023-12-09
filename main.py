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



    self.ui.label_1.mouseDoubleClickEvent = lambda event: self.image_1.browse_file(self.ui.label_1,self.ui.label_2)
    self.ui.label_3.mouseDoubleClickEvent = lambda event: self.image_3.browse_file(self.ui.label_3,self.ui.label_4)
    self.ui.label_5.mouseDoubleClickEvent = lambda event: self.image_5.browse_file(self.ui.label_5,self.ui.label_6)
    self.ui.label_7.mouseDoubleClickEvent = lambda event: self.image_7.browse_file(self.ui.label_7,self.ui.label_8)

    
    self.image_1 = Image()
    self.image_3 = Image()
    self.image_5 = Image()
    self.image_7 = Image()
    self.ui.comboBox_2.currentIndexChanged.connect(lambda index: self.image_3.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_4))
    self.ui.comboBox_3.currentIndexChanged.connect(lambda index: self.image_5.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_6))
    self.ui.comboBox_4.currentIndexChanged.connect(lambda index: self.image_7.plot_spectrum(self.ui.comboBox.currentText(),self.ui.label_8))
    self.ui.comboBox.currentIndexChanged.connect(  lambda index: self.handle_combobox_change(self.ui.label_2))


  def handle_combobox_change(self, spectrum_label):
      try:
          spectrum_type = self.ui.comboBox.currentText()
          self.image_1.plot_spectrum(spectrum_type,spectrum_label)
      except Exception as e:
          print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
