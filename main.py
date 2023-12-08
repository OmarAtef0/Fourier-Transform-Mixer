import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIcon
from task4 import Ui_MainWindow
from images import Image

class FourierTransformMixer(QMainWindow):
  
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  

    self.image_1 = Image()
    self.image_3 = Image()
    self.image_5 = Image()
    self.image_7 = Image()

    self.ui.label_1.mouseDoubleClickEvent = lambda event: self.image_1.browse_file(self.ui.label_1)
    self.ui.label_3.mouseDoubleClickEvent = lambda event: Image.browse_file(self.ui.label_3)
    self.ui.label_5.mouseDoubleClickEvent = lambda event: Image.browse_file(self.ui.label_5)
    self.ui.label_7.mouseDoubleClickEvent = lambda event: Image.browse_file(self.ui.label_7)
      

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = FourierTransformMixer()
  window.setWindowTitle("Fourier Transform Mixer")
  # app.setWindowIcon(QIcon("assets/logo.jpg"))
  window.resize(1450,950)
  window.show()
  sys.exit(app.exec_())
