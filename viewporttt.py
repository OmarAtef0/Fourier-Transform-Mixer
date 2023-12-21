from PyQt5.QtWidgets import QWidget, QFileDialog
from vp import Ui_Viewport
import pyqtgraph as pg
import numpy as np
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QSlider
from PyQt5.QtCore import Qt, QRectF, QObject, QPointF, QMetaProperty, pyqtSignal
from PyQt5.QtWidgets import QMenu, QAction
import logging

logging.basicConfig(filename = 'application.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s', filemode='w')


IMG_IN = "Img In"
IMG_OUT = "Img Out"
RAW_IMG = "Raw Img"
DATA_IMG_ORIG = "Img Data Orig"
DATA_IMG = "Img Data"
DATA_IMG_FT = "Img Data FT"
DATA_IMG_FT_SHIFTED = "Img Data FT Shifted"
FT_MAG = "FT Magnitude"
FT_PHASE = "FT Phase"
FT_REAL = "FT Real"
FT_IMAG = "FT Imaginary"

class SignalEmitter(QObject):
    sig_ROI_changed = pyqtSignal(pg.ROI)
    objectCreated = pyqtSignal()

class Viewport(QtWidgets.QWidget, Ui_Viewport):
    def __init__(self, parent: QWidget | None):
        super(Viewport, self).__init__(parent)
        self.setupUi(self)
        
        # Flags to allow altering the widget's funcionality
        self.ft_enabled = True
        self.can_browse = True
        
        # Signal emiiter class to emit custom signals
        self.sig_emitter = SignalEmitter()
        
        

        self.ROI_Maxbounds = QRectF(0, 0, 100, 100)

        self.brightness_val = 1
        self.contrast_val = 1



        self.img_data = None

        self.img_data_dict = {
            IMG_IN: None,
            IMG_OUT: None,
            RAW_IMG: None,
            DATA_IMG_ORIG: None,
            DATA_IMG: None,
            DATA_IMG_FT: None,
            DATA_IMG_FT_SHIFTED: None,
            FT_MAG: None,
            FT_PHASE: None,
            FT_REAL: None,
            FT_IMAG: None
        }

        self.img_data_modified_dict = {
            IMG_IN: None,
            IMG_OUT: None,
            RAW_IMG: None,
            DATA_IMG_ORIG: None,
            DATA_IMG: None,
            DATA_IMG_FT: None,
            DATA_IMG_FT_SHIFTED: None,
            FT_MAG: None,
            FT_PHASE: None,
            FT_REAL: None,
            FT_IMAG: None
        }

        self.initial_roi_position = None


        self.cmbx_ft.currentIndexChanged.connect(lambda :self.plot_ft_data(self.cmbx_ft.currentText()))
        
        self.image_view = self.plot_img.addViewBox()
        self.image_view.setAspectLocked(True)
        self.image_view.setMouseEnabled(x=False, y=False)
        self.image_view.setMenuEnabled(False)
            
        self.ft_view = self.plot_ft.addViewBox()
        self.ft_view.setAspectLocked(True)
        self.ft_view.setMouseEnabled(x=False, y=False)
        self.ft_view.setMenuEnabled(False)

        
        self.img_item = pg.ImageItem()
        self.img_item_ft = pg.ImageItem()
        self.image_view.addItem(self.img_item)
        self.ft_view.addItem(self.img_item_ft)

        
        #ft_view (viewbox)--> by carry img_item & img_item_ft
        
        # Creating ROI
        self.ft_roi = pg.ROI(pos = self.ft_view.viewRect().center(), size = (50, 50), hoverPen='b', resizable= True, invertible= True, rotatable= False, maxBounds= self.ROI_Maxbounds)
        #whats ft_view
        self.ft_view.addItem(self.ft_roi)
        self.add_scale_handles_ROI(self.ft_roi)      
        

        
        # Connecting ROI signal to update region of data selected
        self.ft_roi.sigRegionChangeFinished.connect(lambda: self.region_update(finish = True))
        
        # Connect doubleClicked signal to the custom slot
        self.plot_img.scene().sigMouseClicked.connect(self.open_Img_file)


        self.plot_img.scene().sigMouseClicked.connect(lambda event: self.reset_brightness_contrast() if event.button() == 2 else None)
        self.plot_ft.scene().sigMouseClicked.connect(lambda event: self.reset_ROI() if event.button() == 2 else None)



        # Override the mouseMoveEvent method to prevent default behavior
        self.img_item.mouseDragEvent = self.mouse_drag_bright_change
        
        
        # Load default image
        img_path = 'Boxx.png'
        self.load_image(img_path)
        
    
    def region_update(self, finish=False):
        if finish:
            self.sig_emitter.sig_ROI_changed.emit(self.ft_roi)
        self.img_data_modified_dict[IMG_OUT], self.img_data_modified_dict[IMG_IN] =  np.fft.ifft2(np.fft.ifftshift(self.return_region_slice()))
        logging.debug('Region update finished')

    def return_region_slice(self):
        data = self.img_data_dict[DATA_IMG_FT_SHIFTED]
        data_slice_indices, QTrans = self.ft_roi.getArraySlice(data, self.img_item_ft, returnSlice=True)
        mask = np.full(data.shape, False)
        mask[data_slice_indices] = True
        masked_data_in = data * mask
        masked_data_out = data.copy()
        masked_data_out[mask] = 0
        logging.debug('Region slice returned')
        return (masked_data_in, masked_data_out)

    

    

   


    
##===============================## Helper Functions ##===============================##
    
    def add_scale_handles_ROI(self, roi : pg.ROI):
        positions = np.array([[0,0], [1,0], [1,1], [0,1]])
        for pos in positions:        
            roi.addScaleHandle(pos = pos, center = 1 - pos)
            
    
    def center_ROI_to_image(self):
        roi_rect = self.ft_roi.size()
        half_width = roi_rect[0] / 2
        half_height = roi_rect[1] / 2
        center = self.img_item_ft.boundingRect().center()
        adjusted_center = [center.x() - half_width, center.y()- half_height]
        self.ft_roi.setPos(adjusted_center)
        logging.debug('ROI centered to image')
        
        
    def set_ROI_size_to_image(self):
        self.ft_roi.setSize(size=(self.img_item_ft.boundingRect().width(), self.img_item_ft.boundingRect().height()))
        logging.debug('ROI size set to image size')
        
        
    def reset_ROI(self):
        self.set_ROI_size_to_image()
        self.center_ROI_to_image()
        logging.debug('Reset ROI')
        
    def set_properties(self):
        self.ft_enabled = self.property('ft_enabled')
        self.can_browse = self.property('can_browse')
        self.wgt_ft.setVisible(self.ft_enabled)
        logging.debug(f'Properties set: ft_enabled={self.ft_enabled}, can_browse={self.can_browse}')

           




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Viewport(None)
    window.show()
    app.exec_()