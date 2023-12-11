import numpy as np
import cv2
import matplotlib.pyplot as plt

def plot_image_properties(image):
    # Calculate the 2D FFT
    fft_image = np.fft.fft2(image)

    # Shift the zero frequency component to the center
    fft_image_shifted = np.log(np.fft.fftshift(fft_image)+1)

    # Magnitude spectrum
    magnitude_spectrum = np.abs(fft_image_shifted)
    plt.subplot(2, 2, 1)
    plt.imshow(np.multiply(np.log(1 + magnitude_spectrum),20), cmap='gray')
    plt.title('Magnitude Spectrum')
    
    # Phase spectrum
    phase_spectrum = np.angle(fft_image_shifted)
    plt.subplot(2, 2, 2)
    plt.imshow(phase_spectrum, cmap='gray')
    plt.title('Phase Spectrum')

    # Real part
    real_part = np.real(fft_image_shifted)

    plt.subplot(2, 2, 3)
    plt.imshow(real_part, cmap='gray')
    plt.title('Real Part')

    # Imaginary part
    imag_part = np.imag(fft_image_shifted)
    plt.subplot(2, 2, 4)
    plt.imshow(imag_part, cmap='gray')
    plt.title('Imaginary Part')

    print("REAL PART:",real_part, "And its shape is:",real_part.shape)
    print("mag shape:", magnitude_spectrum.shape)
    print("imaginary shape:", imag_part.shape)
    print("Phase shape:", phase_spectrum.shape)
    plt.show()

# Example usage with a random image (replace this with your image)
your_image = cv2.imread("C:/Users/khale/Desktop/test1.jpg", cv2.IMREAD_GRAYSCALE)
plot_image_properties(your_image)
