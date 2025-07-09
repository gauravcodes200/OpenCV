# Interactive Image Capture with OpenCV

## Overview<br>

This project provides a simple yet effective solution for capturing high-quality images from your webcam using Python and OpenCV on Linux systems. The script features a live preview window, and allows the user to capture images by pressing the **SPACE** key. Each captured image is saved with a timestamped filename, ensuring uniqueness and easy file management.<br>

## Features<br>

- **Live Preview:** Real-time display of the video feed from your webcam.<br>
- **Interactive Capture:** Capture an image by pressing the **SPACE** key.<br>
- **Keyboard Controls:** Use **'q'** to exit the session.<br>
- **High Resolution:** The webcam is set to capture images in a high resolution (1280x720).<br>
- **Timestamped Filenames:** Each captured image is saved with a unique filename based on the current datetime.<br>
- **Quality Settings:** JPEG output is saved with maximum quality.<br>

## Prerequisites<br>

- **Linux Operating System:** This script is designed for Linux-based systems.<br>
- **Python 3:** Ensure that Python 3 is installed on your system.<br>
- **OpenCV:** Install the OpenCV Python module by running:<br>
  ```bash
  pip install opencv-python
  ```
Controls:<br>

SPACE Key: Capture the current frame and save the image with a timestamped filename.<br>

q Key: Quit the program and close the preview window.<br>

Output:<br>
Captured images will be saved in the current directory with filenames similar to image_20250709_220134.jpg.<br>

Future Enhancements<br>
Countdown Timer: Add a visual countdown before capturing an image.<br>

Overlay Guides: Incorporate overlay guides or framing boxes to assist in positioning.<br>

Configuration File: Implement a configuration file to allow dynamic adjustment of settings.<br>

GUI Improvements: Develop a more advanced GUI using libraries such as PyQt for extended functionality.<br>

Integration with Audio: Expand the functionality to record audio concurrently for multimedia applications.<br>


<h1>Output</h1>



https://github.com/user-attachments/assets/09d3ce35-7765-442e-9188-f55812244823

![image_20250709_220654](https://github.com/user-attachments/assets/ba2a7672-70dd-48bd-8afd-b9da650dcba2)
![image_20250709_220650](https://github.com/user-attachments/assets/2c1f33ac-e603-4904-b49f-41bb4578d091)




