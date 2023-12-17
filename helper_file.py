from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPointF, QRectF

class ROIWidget(QLabel):
    def __init__(self, parent=None):
        super(ROIWidget, self).__init__(parent)
        self.setPixmap(QPixmap("assets/img_1.jpg"))  # Replace with the path to your image
        self.roi_rect = QRectF(50, 50, 100, 100)
        self.dragging = False
        self.resize_handle_pressed = False
        self.last_pos = QPointF()

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.resize_handle_rect().contains(event.pos()):
                self.resize_handle_pressed = True
            elif self.roi_rect.contains(event.pos()):
                self.dragging = True
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.pos() - self.last_pos
            self.roi_rect.translate(delta)
            self.update()
        elif self.resize_handle_pressed:
            delta = event.pos() - self.last_pos
            # self.roi_rect.adjust(0, 0, delta.x(), delta.y())
            self.roi_rect.setBottomRight(event.pos())
            self.update()
        self.last_pos = event.pos()

    def mouseReleaseEvent(self, event):
        self.dragging = False
        self.resize_handle_pressed = False

    def paintEvent(self, event):
        super(ROIWidget, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the ROI rectangle
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.roi_rect)

        # Draw the resize handle
        painter.setBrush(Qt.red)
        painter.drawRect(self.resize_handle_rect())

    def resize_handle_rect(self):
        handle_size = 10
        return QRectF(self.roi_rect.bottomRight().x() - handle_size,
                      self.roi_rect.bottomRight().y() - handle_size,
                      handle_size,
                      handle_size)

    def resize_roi(self, width=200, height=200):
        self.roi_rect.setWidth(width)
        self.roi_rect.setHeight(height)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.roi_widget = ROIWidget()
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.roi_widget)
        self.setCentralWidget(central_widget)


    # def timerEvent(self, event):
    #     # Example: Resize the ROI to 150x150
    #     self.roi_widget.resize_roi(150, 150)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
