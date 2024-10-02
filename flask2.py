import requests
from PIL import Image
from io import BytesIO
from sun_Detector import *
# Flask (ESP32 simulation) URL
flask_url = "http://localhost:5000/capture"  # Replace with Flask server's address
sun_detector = SunDetector()


def capture_and_process_image():
    response = requests.get(flask_url)

    if response.status_code == 200:
        # Load the image from the response content using PIL
        image = Image.open(BytesIO(response.content))

        # Save the image locally with a fixed name
        image.save("latest_image.jpg")
        print("Image saved as latest_image.jpg")

        
        frames = [cv2.imread('latest_image.jpg')]  # Example images

        for i, frame in enumerate(frames):
          if frame is not None:
             sun_detector.set_frame(frame)   # Set the current frame
             sun_detector.find_sun()         # Detect the sun in the frame
             sun_detector.display(f"Sun Detection - Frame {i+1}")

             output_filename = f"processed_image.jpg"
             sun_detector.save_output(output_filename)
        print("Processed image saved as processed_image.jpg")

        # Store results
        with open("processing_results.txt", "w") as file:
            file.write("processing complete.\n")
        print("Processing results saved in processing_results.txt")
    else:
        print("Failed to retrieve image from Flask server")

# Test the image capture and processing
capture_and_process_image()
