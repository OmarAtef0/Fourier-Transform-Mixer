import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
import pyqtgraph as pg

class ImageDisplay(QWidget):
    def __init__(self):
        super().__init__()

        # Create QLabel for image display
        self.label_viewport = QLabel()
        self.label_viewport.setAlignment(Qt.AlignCenter)

        # Create PyQtGraph ImageView for image display
        self.graph_viewport = pg.ImageView()

        # Create layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label_viewport)
        layout.addWidget(self.graph_viewport)

        # Connect double-click events to open file dialog
        self.label_viewport.mouseDoubleClickEvent = self.open_image_dialog
        self.graph_viewport.scene.sigMouseClicked.connect(self.open_image_dialog)

    def open_image_dialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)

        if file_name:
            # Load image to QLabel
            pixmap = QPixmap(file_name)
            self.label_viewport.setPixmap(pixmap.scaled(self.label_viewport.size(), Qt.KeepAspectRatio))

            # Load image to PyQtGraph ImageView
            img = pg.ImageItem()
            img.setImage(QImage(file_name))
            self.graph_viewport.addItem(img)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = ImageDisplay()
        self.setCentralWidget(self.central_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
