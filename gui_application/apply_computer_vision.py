import cv2
import numpy as np


class ComputerVision:
    def __init__(self):
        self.source_path = "images_for_application/nature_image.png"
        self.image = np.ndarray
        self.grayscale_image = np.ndarray
        self.blur_image = np.ndarray
        self.threshold_images = np.ndarray
        self.contours = np.ndarry
        self.hierarchy = np.ndarray

    def get_image(self) -> np.ndarray:
        # Getting the image from the source path
        self.image = cv2.imread(self.source_path)

        return self.image

    def gray_scale(self, image: np.ndarray) -> np.ndarray:
        # Getting the grayscale image
        self.grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return self.grayscale_image

    def gaussian_blur(self, gray_scale_image: np.ndarray) -> np.ndarray:
        # Creating a kernel
        kernel = (5, 5)

        # Getting the blur image
        self.blur_image = cv2.GaussianBlur(gray_scale_image, kernel, 0)

        return self.blur_image

    def get_threshold(self, blur_image: np.ndarray) -> np.ndarray:
        # Getting the threshold image
        ret, self.threshold_images = cv2.threshold(blur_image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

        return self.threshold_images

    def find_contours(self, threshold_image: np.ndarray) -> np.ndarray:
        # Getting the contours from the image
        self.contours, self.hierarchy = cv2.findContours(threshold_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        return self.contours, self.hierarchy

    def plot_two_images(self, threshold_image: np.ndarray, contours: np.ndarray):
        # Plotting image and contours
        image = cv2.drawContours(threshold_image, contours, -1, (0, 255, 0), 3)

        # Plot image
        cv2.imshow("Image and Contours", image)
        cv2.waitKey(0)

    def plot_one_image(self, image: np.ndarray):
        # Plotting the image
        cv2.imshow("Image", image)
        cv2.waitKey(0)



