import cv2
from gtts import gTTS
import os
from picamera2 import Picamera2
import numpy as np
from paddleocr import PaddleOCR

# Initialize the PaddleOCR model
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # You can specify different languages if needed

def recognize_text(image):
    # Use PaddleOCR to recognize text
    result = ocr.ocr(image, cls=True)
    
    # Extract and format the recognized text
    recognized_text = ""
    for line in result:
        for word in line:
            recognized_text += word[1][0] + " "  # Word and its confidence
    return recognized_text.strip()

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("/tmp/speech.mp3")
    os.system("mpg321 /tmp/speech.mp3")

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply adaptive thresholding to enhance text
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    return thresh

def main():
    picam2 = Picamera2()

    # Set the desired resolution
    width, height = 640, 480  # Lower resolution for faster processing

    # Create a preview configuration with the desired resolution
    preview_config = picam2.create_preview_configuration(main={"size": (width, height)})
    picam2.configure(preview_config)
    picam2.start()

    frame_skip = 30  # Number of frames to skip between OCR calls
    frame_count = 0

    while True:
        frame = picam2.capture_array()

        if frame is None:
            print("Error: Could not capture frame.")
            break

        cv2.imshow('frame', frame)

        # Only process every frame_skip-th frame for OCR
        if frame_count % frame_skip == 0:
            # Pre-process the frame
            processed_frame = preprocess_image(frame)

            # Process the captured frame
            text = recognize_text(processed_frame)
            if text:
                print(f"Recognized Text: {text}")

                # Convert recognized text to speech
                text_to_speech(text)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    picam2.stop()

if __name__ == "__main__":
    main()
