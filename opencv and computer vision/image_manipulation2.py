import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:\\Users\\User\\Desktop\\AI\\opencv and computer vision\\image2.jpg')
plt.imshow(image)
plt.title("OG image")
plt.show()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_scale, cmap='gray')
plt.title('Gray-scale image')
plt.show()

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_scale)
plt.title('Grayscale image')
plt.show()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
plt.imshow(hsv_image)
plt.title("Hsv image")
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped region")
plt.show()