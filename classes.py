import cv2
import numpy as np 

class image():
    def __init__(self, index):
        self.index = index
        self.path = None
        self.name = None
        self.fft = None
        self.fft_shift = None
        self.shape = None
        self.fft_phase = None
        self.fft_mag = None
        self.fft_real = None
        self.fft_imag = None
        
    def browse_image(self):
        pass
        
    def read_image(self):
        pass
    
    def compute_fourier_transform(self):
        pass
    
    def reshape(self):
        pass
    
    def change_brightness(self):
        pass
    
    def change_contrast(self):
        pass
    
    
class Mixer(self):
    pass