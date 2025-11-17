import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype('uint88'), sobely.astype('uint8'))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2RGB)
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return filtered_image

image_path = "C:\\Users\\User\\Desktop\\AI\\opencv and computer vision\\image2.jpg"
image = cv2.imread(image_path)
if image is None:
    print("Error 404: Image Not Found!!!, Check for errors!!!")
else:
    filter_type = "original"
    print("press a key from the list given to filter the image")
    print("r - Red Tint\ng - Green Tint\nb - Blue Tint\ns - Sobel Edge detection\nc - Canny Edge Detectin\nq - Quit")

    while True:
                filtered_image = apply_filter