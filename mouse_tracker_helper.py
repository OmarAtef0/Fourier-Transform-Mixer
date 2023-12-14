import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget 
from PyQt5.QtGui import QPixmap, QMouseEvent , QImage
from PyQt5 import QtCore
from image import Image

class ImageDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create labels and set image paths
        self.x = None
        self.y = None
        self.image = Image()
        self.image.load_image("assets/img_3.jpg")
        image_path1 = "assets/img_3.jpg"
        image_path2 = "assets/img_3.jpg"
        self.label1 = QLabel(self)
        label2 = QLabel(self)

        # Set images to labels
        self.set_image(self.label1, image_path1)
        self.set_image(label2, image_path2)

        # Set red background color for labels
        self.label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: red;")

        # Create a vertical layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label1)
        layout.addWidget(label2)
        layout.setAlignment(self.label1, QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(label2, QtCore.Qt.AlignmentFlag.AlignCenter)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Image Display App")
        self.setGeometry(100, 100, 800, 600)


    def set_image(self, label, image_path):
        # Set image to the label
        # print(f'shape {self.image.get_img().shape}')
        width , height = self.image.get_img().shape
        q_image = QImage(self.image.get_img().tobytes(), width, height, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(q_image)
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Variable to track mouse movement
        self.mouse_pressed = False
    def mousePressEvent(self, event: QMouseEvent):
        if (
            event.button() == QtCore.Qt.MouseButton.LeftButton
            and self.label1.geometry().contains(event.pos())
        ):
            self.mouse_pressed = True
            self.track_mouse_position(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.mouse_pressed:
            self.track_mouse_position(event)

    def track_mouse_position(self, event: QMouseEvent):
        # Track mouse position when clicking and holding on label1
        crrX, crrY = event.pos().x(), event.pos().y()
        # print(f"Mouse Position: ({crrX}, {crrY})")
        if self.x is None:
            self.x = crrX
            self.y = crrY
        else:
            if crrX - self.x > 5:
                print("Right") #call brightness functon instead
            elif crrX - self.x < -5:
                print("Left") #call brightness functon instead
            self.x = crrX
            if crrY - self.y > 5:
                print("Down")#call contrast functon instead
            elif crrY - self.y < -5:
                print("Up")#call contrast  functon instead
            self.y = crrY
        print(f"Mouse Position: ({self.x}, {self.y})")
        
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.mouse_pressed = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageDisplayApp()
    window.show()
    sys.exit(app.exec())
