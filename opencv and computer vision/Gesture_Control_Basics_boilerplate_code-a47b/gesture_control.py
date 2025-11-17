# TODO: Import cv2 for computer vision and numpy for numerical operations.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contours = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contours) > 500:
            x, y, w, h = cv2.boundingRect(max_contours)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            center_x = int(x + w / 2)
            center_y = int(y + w / 2)
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
        
    cv2.imshow('Original Frame', frame)
    cv2.imshow('filtered Frame', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# TODO: Initialize webcam capture using cv2.VideoCapture(0).
#       - If the webcam fails to open, print an error message and exit the program.

# TODO: Start an infinite loop to continuously process frames from the webcam:
    # TODO: Capture a frame from the webcam using cap.read().
    #       - If frame capture fails, print an error message and break the loop.
    
    # TODO: Convert the captured frame from BGR color space to HSV color space using cv2.cvtColor.
    
    # TODO: Define the lower and upper HSV bounds for skin color detection.
    
    # TODO: Create a mask using cv2.inRange() with the defined HSV bounds to identify skin-colored regions.
    
    # TODO: Apply the mask to the original frame using cv2.bitwise_and() to extract the skin regions.
    
    # TODO: Find contours in the masked image using cv2.findContours() to detect hand shapes.
    
    # TODO: If any contours are found:
        # TODO: Identify the largest contour based on its area.
        # TODO: Check if the area of the largest contour is above a minimum threshold (e.g., 500).
        # TODO: If the contour is large enough:
            # TODO: Compute the bounding rectangle for the largest contour using cv2.boundingRect().
            # TODO: Draw the bounding rectangle on the original frame with cv2.rectangle().
            # TODO: Calculate the center of the bounding box.
            # TODO: Draw a small circle at the center of the detected hand using cv2.circle().
    
    # TODO: Display the original frame and the filtered frame (showing only skin regions) using cv2.imshow().
    
    # TODO: Wait briefly for a key press using cv2.waitKey(1); if the 'q' key is pressed, break out of the loop.

# TODO: After the loop ends, release the webcam and close all OpenCV windows using cap.release() and cv2.destroyAllWindows().
