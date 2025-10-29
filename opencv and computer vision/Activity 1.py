import cv2

image = cv2.imread('C:\\Users\\User\\Desktop\\AI\\opencv and computer vision\\image.jpg')

cv2.namedWindow('Image Example', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Image Example', 800, 500)

cv2.imshow('Image Example', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Image Dimensions = {image.shape}")