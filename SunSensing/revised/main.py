from sun_Detector import *
import cv2
import numpy as np
import time
from lmaowut import*

sun_detector = SunDetector()

# For each frame (image), process it individually
frames = [cv2.imread('frame1.jpg'), cv2.imread('frame2.jpg'), cv2.imread('frame4.jpg')]  # Example images

for i, frame in enumerate(frames):
    if frame is not None:
        sun_detector.set_frame(frame)   # Set the current frame
        fx , fy = sun_detector.find_sun()         # Detect the sun in the frame
        
        print(fx,fy)
        pos  = [fx,fy]

        servoX = np.interp(fx , [0,sun_detector.get_frame_width()] , [180,0])
        servoY = np.interp(fy , [0,sun_detector.get_frame_height()] , [180,0])
        if servoX < 0:
            servoX = 0
        elif servoX > 180:
            servoX = 180
        if servoY < 0:
            servoY = 0
        elif servoY > 180:
            servoY = 180
        
        pos[0] = servoX
        pos[1] = servoY

        print(pos)
        cv2.putText(frame, f'Servo X: {int(pos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.putText(frame, f'Servo Y: {int(pos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        print(sun_detector.get_frame_center())

        sun_detector.display(f"Sun Detection - Frame {i+1}")  # Display the result with the sun center drawn

# Process additional frames as necessary...