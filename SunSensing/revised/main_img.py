from sun_Detector import *
import cv2
import numpy as np

# Initialize the sun detector
sun_detector = SunDetector()

# List of image file paths
image_files = ['sun_640.jpg']  # Replace with your image paths

# Process each image
for i, image_file in enumerate(image_files):
    frame = cv2.imread(image_file)  # Read the image
    if frame is None:
        print(f"Error: Could not read image {image_file}.")
        continue

    sun_detector.set_frame(frame)   # Set the current frame
    fx, fy = sun_detector.find_sun()  # Detect the sun in the frame

    print(f"Sun center found at: {fx}, {fy}")
    pos = [fx, fy]

    # Map coordinates to servo angles
    AngleX = np.interp(fx, [0, sun_detector.get_frame_width()], [180, 0])
    AngleY = np.interp(fy, [0, sun_detector.get_frame_height()], [180, 0])



    pos[0] = AngleX
    pos[1] = AngleY
    print(int(pos[0]))
    print(int(pos[1]))


    # Draw the circle at the sun's location
    if fx is not None and fy is not None:
        cv2.circle(frame, (int(fx), int(fy)), 80, (0, 0, 255), 2)  # Draw the outer circle
        cv2.circle(frame, (int(fx), int(fy)), 15, (0, 0, 255), cv2.FILLED)  # Draw the inner circle
        cv2.circle(frame, (int(sun_detector.frameCenter[0]), int(int(sun_detector.frameCenter[1]))), 5, (0, 0, 255), cv2.FILLED)  # Draw the outer circle
        
        cv2.putText(frame, f'Angle X: {int(pos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(frame, f'Angle Y: {int(pos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # Display the frame with the drawn elements
    cv2.imshow(f"Sun Detection - Image {i + 1}", frame)

    # Wait for a key press for a short duration to visualize the result
    cv2.waitKey(0)  # Display each image for 1 second (adjust as needed)

# Close all OpenCV windows
cv2.destroyAllWindows()
