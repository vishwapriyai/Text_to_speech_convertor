# Real-Time Text Recognition and Speech Synthesis

## Overview
This project implements a real-time text recognition system using a Raspberry Pi camera and PaddleOCR. The recognized text is then converted to speech using the Google Text-to-Speech (gTTS) library. This application can be useful for visually impaired individuals or for any scenario where text needs to be read aloud.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  
## Features
- Real-time text recognition from camera feed.
- Text-to-speech conversion of recognized text.
- Image preprocessing to enhance text recognition accuracy.
- Configurable frame capture rate for OCR processing.

## Technologies Used
- **Python**: The primary programming language used for implementation.
- **OpenCV**: For capturing and processing video frames.
- **PaddleOCR**: For optical character recognition.
- **gTTS (Google Text-to-Speech)**: For converting text to speech.
- **Picamera2**: For interfacing with the Raspberry Pi camera.

## Usage
1. Connect your Raspberry Pi camera and ensure it is functioning correctly.
2. Run the script:
   ```bash
   python text_recognition.py
   ```

## Usage
The application will start capturing video frames. It will recognize text in the frames and read it aloud.  
Press 'q' to exit the application.

## Code Explanation
- **Text Recognition**: The `recognize_text` function uses PaddleOCR to extract text from the processed image.
- **Text-to-Speech**: The `text_to_speech` function converts the recognized text into speech and plays it back.
- **Image Preprocessing**: The `preprocess_image` function converts the image to grayscale, applies Gaussian blur, and uses adaptive thresholding to enhance text visibility.
- **Main Loop**: The `main` function captures frames from the camera, processes them for OCR, and reads the recognized text aloud.
