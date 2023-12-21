import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsRectItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF

class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super(ImageViewer, self).__init__(parent)

        # Create a scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Load an image
        pixmap = QPixmap("assets/img_2.jpg")
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)

        # Add a rectangular ROI
        roi_rect = QGraphicsRectItem(QRectF(100, 100, 200, 200))  # Define the ROI rect
        roi_rect.setPen(Qt.red)  # Set the pen color for the ROI
        self.scene.addItem(roi_rect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec_())
