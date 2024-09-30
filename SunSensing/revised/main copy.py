from sun_Detector import *
import cv2
import numpy as np

# Initialize the sun detector
sun_detector = SunDetector()

# Open a video file or capture from the webcam
video_source = 'sun_no_clouds.mp4'  # Replace with 0 for webcam or provide video file path
cap = cv2.VideoCapture(video_source)
fps = cap.get(cv2.CAP_PROP_FPS)
wait_time = int(1000 / fps)
# Check if the video source is opened correctly
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Process each frame from the video
while True:
    ret, frame = cap.read()  # Read a frame from the video
    if not ret:
        print("End of video or error reading frame.")
        break  # Exit the loop if no more frames

    sun_detector.set_frame(frame)   # Set the current frame
    fx, fy = sun_detector.find_sun()  # Detect the sun in the frame

    print(fx, fy)
    pos = [fx, fy]

    # Map coordinates to servo angles
    servoX = np.interp(fx, [0, sun_detector.get_frame_width()], [180, 0])
    servoY = np.interp(fy, [0, sun_detector.get_frame_height()], [180, 0])

    # Clamp servo angles to the valid range
    #servoX = np.clip(servoX, 0, 180)
    #servoY = np.clip(servoY, 0, 180)

    pos[0] = servoX
    pos[1] = servoY

    # Draw the circle at the sun's location
    if fx is not None and fy is not None:
        cv2.circle(frame, (int(fx), int(fy)), 80, (0, 0, 255), 2)  # Draw the outer circle
        cv2.circle(frame, (int(fx), int(fy)), 15, (0, 0, 255), cv2.FILLED)  # Draw the inner circle
        cv2.putText(frame, f'Servo X: {int(pos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(frame, f'Servo Y: {int(pos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # Display the frame with the drawn elements
    cv2.imshow("Sun Detection", frame)

    # Break the loop on 'q' key press
    
    if cv2.waitKey(wait_time) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
