import cv2
import numpy

source_path = r"code_and_pictures/mri_testing_images/patient1R.png"
image = cv2.imread(source_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
ret, threshold = cv2.threshold(blur_image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

big_contour = []

for index in contours:
    area = cv2.contourArea(index)
    if area > 1000:
        big_contour.append(index)

image = cv2.drawContours(image, big_contour, -1, (0, 255, 0), 3)

cv2.imshow("An image", image)
cv2.waitKey(0)
