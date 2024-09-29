import cv2
import numpy as np

class SunDetector:
    def __init__(self):
        self.frame = None
        self.gry_img = None
        self.blurredImage = None
        self.threshold_img = None
        self.sunCenter = None
        self.frameCenter = None

    # Setters
    def set_frame(self, frame):
        self.frame = frame
        self.set_frame_center()

    def set_sun_center(self, center):
        self.sunCenter = [center[0], center[1]]

    def set_frame_center(self):
        if self.frame is not None:
            height, width = self.frame.shape[:2]
            self.frameCenter = [width // 2, height // 2]

    # Getters
    def get_frame(self):
        return self.frame

    def get_sun_center(self):
        return self.sunCenter

    def get_frame_center(self):
        return self.frameCenter

    def get_frame_width(self):
        return self.frame.shape[1] if self.frame is not None else None

    def get_frame_height(self):
        return self.frame.shape[0] if self.frame is not None else None

    # Method to find sun
    def find_sun(self):
        if self.frame is not None:
            self.gry_img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.blurredImage = cv2.GaussianBlur(self.gry_img, (15, 15), 0) #gaussian filter
            _, self.threshold_img = cv2.threshold(self.blurredImage, 240, 255, cv2.THRESH_BINARY)

            # Find contours to detect the sun
            contours, _ = cv2.findContours(self.threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                largest_contour = max(contours, key=cv2.contourArea)
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    self.set_sun_center((cx, cy))
                    print(f"Sun center found at: {self.sunCenter}")
 # Draw a circle at the detected sun center
                    cv2.circle(self.frame, (cx, cy), 20, (0, 0, 255), 3)  # Red circle with a radius of 20
                    cv2.putText(self.frame, f"Sun Center: ({cx}, {cy})", (cx - 50, cy - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                else:
                    print("No valid sun center found.")
            else:
                print("No contours found for sun detection.")

    # Display frame
    def display(self, action):
        if self.frame is not None:
            cv2.imshow(action, self.frame)
            cv2.waitKey(1)  # Display for a brief moment, since you'll likely be working with continuous frames

# Example usage:
# Capture frames from a video or camera feed
cap = cv2.VideoCapture(1)  # camera feed 0:Primary 1:Secondary
sun_detector = SunDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    sun_detector.set_frame(frame)
    sun_detector.find_sun()
    sun_detector.display("Sun Detection")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
