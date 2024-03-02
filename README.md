# Fourier Fusion Lab
- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

**Fourier Fusion Lab** is an advanced desktop application meticulously designed to demonstrate the intricate interplay between magnitude and phase components in signals, with a particular emphasis on frequency contributions. This software focuses on 2D signals (images), but the concepts apply to any type of signal. The program provides a feature-rich environment for viewing, customizing, and mixing grayscale images.


## Features

### Image Viewers

1. **Image Exploration and Visualization:**
   - Seamlessly open and view up to four grayscale images simultaneously, each meticulously presented in its dedicated viewport.
   - Enjoy a cohesive viewing experience as images are dynamically resized to match the smallest size among all opened images.

2. **Insightful Fourier Transform (FT) Component Display:**
   - Gain deeper insights into signal characteristics with per-image viewport displays showcasing Fourier Transform components, including Magnitude, Phase, Real, and Imaginary parts.

3. **Intuitive Image Navigation:**
   - Effortlessly navigate between images by double-clicking on the respective viewer, triggering a tailored browsing function exclusive to each image.

### Output Ports

4. **Streamlined Output Display:**
   - Utilize two output viewports mirroring the input image viewports, offering precise control over the display of newly generated mixer results.

### Fine-tuned Brightness/Contrast Adjustment

5. **Precision Image Enhancement Controls:**
   - Fine-tune brightness and contrast levels with intuitive controls applicable to all four image components, ensuring optimal visualization and analysis.

### Components Mixer

6. **Tailored Weighted Averaging:**
   - Unlock creativity with an advanced mixer generating output images from the inverse Fourier transform of a meticulously weighted average of the Fourier Transforms of the four input images.
   - Customize weights assigned to each image's Fourier Transform using intuitive sliders for unparalleled creative control.

### Regions Mixer

7. **Selective Frequency Region Manipulation:**
   - Exercise precise control over signal frequencies by selecting regions of interest for each Fourier Transform component, whether exploring the depths of low frequencies or the heights of high frequencies.

### Real-time Mixing

8. **Seamless Real-time Operations:**
   - Stay informed with a dynamic progress bar providing real-time updates on ongoing mixing processes, ensuring a seamless user experience even during resource-intensive operations.

## Live Demo

https://github.com/OmarAtef0/Fourier-Transform-Mixer/assets/100636693/61165d64-174f-4378-a107-bc93944cf34e

## Installation

1. Clone the repository:


2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program:

   ```bash
   python main.py
   ```



## Contributors

We would like to acknowledge the following individuals for their contributions:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/OmarAtef0" target="_black">
      <img src="https://avatars.githubusercontent.com/u/131784941?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Omar Atef</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/IbrahimEmad11" target="_black">
      <img src="https://avatars.githubusercontent.com/u/110200613?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ibrahim Emad</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Hazem-Raafat" target="_black">
      <img src="https://avatars.githubusercontent.com/u/100636693?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Hazem Rafaat</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Ahmedkhaled222" target="_black">
      <img src="https://avatars.githubusercontent.com/u/109425772?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ahmed Khaled</b></sub></a>
    </td>  
  </tr>
 </table>

## License

<p>This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to use, modify, and distribute this software according to the terms of the license.</p>


## Acknowledgments

This project was supervised by Dr. Tamer Basha & Eng. Abdallah Darwish as a part of Digital Signal Processing course at Cairo University Faculty of Engineering.

<div style="text-align: center">
    <img src="https://imgur.com/Wk4nR0m.png" alt="Cairo University Logo" width="100" style="border-radius: 50%;"/>
</div>

---
