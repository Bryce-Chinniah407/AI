# --------------------------------------------------------------
# Import necessary libraries for:
# 1. Image processing (OpenCV)
# 2. Numerical operations (NumPy)
# 3. Displaying images (Matplotlib)
# --------------------------------------------------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt
# --------------------------------------------------------------
# Define a utility function to display images using Matplotlib.
# 1. Set up the figure size.
# 2. Check if image is grayscale or color.
# 3. Convert color images from BGR to RGB for correct rendering.
# 4. Set the plot title and hide the axis.
# 5. Display the image on the screen.
# --------------------------------------------------------------
def display_image(title, image):
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()
# --------------------------------------------------------------
# Define the main interactive function for edge detection.
# 1. Load an image from a specified path.
# 2. Convert it to grayscale.
# 3. Show the grayscale image to the user.
# 4. Present a menu of operations:
#    a) Sobel Edge Detection
#    b) Canny Edge Detection
#    c) Laplacian Edge Detection
#    d) Gaussian Smoothing
#    e) Median Filtering
#    f) Exit
# 5. Prompt the user to pick an option.
# 6. Perform the chosen operation and display the result.
# 7. Repeat until the user decides to exit.
# --------------------------------------------------------------
def apply_edge_detection(image, method="sobel", ksize=3, threshold1=100, threshold2=200):
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if method == "sobel":
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=ksize)
        return cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
    elif method == "canny":
        return cv2.Canny(gray_image, threshold1, threshold2)
    elif method == "laplacian":
        return cv2.Laplacian(gray_image, cv2.CV_64F).astype(np.uint8)
# --------------------------------------------------------------
# Sobel Edge Detection:
# 1. Calculate Sobel filters along the x and y directions.
# 2. Convert both results to 8-bit images.
# 3. Combine them using bitwise OR.
# 4. Display the combined edge map.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Canny Edge Detection:
# 1. Ask for lower and upper thresholds.
# 2. Apply Canny edge detection, which:
#    - Smooths the image with a Gaussian filter.
#    - Finds intensity gradients.
#    - Applies non-maximum suppression.
#    - Uses double-thresholding and edge tracking.
# 3. Display the detected edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Laplacian Edge Detection:
# 1. Apply the Laplacian operator (second derivative).
# 2. Take the absolute value of the result to handle negative gradients.
# 3. Convert to 8-bit for display.
# 4. Show the resulting edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Gaussian Smoothing:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply GaussianBlur with the specified kernel.
# 3. Display the smoothed image, which helps reduce noise.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Median Filtering:
# 1. Prompt the user for a kernel size (odd number).
# 2. Apply medianBlur, which replaces each pixel with the median of neighbors.
# 3. This helps remove salt-and-pepper noise while preserving edges.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Exit:
# 1. Print a message confirming exit.
# 2. Break out of the interactive loop.
# --------------------------------------------------------------

# --------------------------------------------------------------
# Make a call to the interactive function with the path to an image.
# e.g., interactive_edge_detection("example.jpg")
# This is where the program starts running and awaits user input.
# --------------------------------------------------------------
def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error 404: Image not found. check the image path for any errors")
        return
    print("Select an option:\n 1/. Sobel Edge Detection \n 2/. Canny Edge Detection\n 3/. Laplacian Edge Detection\n 4/. EXIT")
    while True:
        choice = input("Pls Choose An option(1-6)")
        if choice == "1":
            ksize = int(input("Enter kernel size for Sobel (Has to be an odd number)"))
            result = apply_edge_detection(image, method="Sobel", ksize=ksize)
            display_image("Sobel Edge Detection", result)
        elif choice == "2":
            threshold1 = int(input(""))