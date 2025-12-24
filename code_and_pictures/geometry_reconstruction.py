from typing import Tuple
import cv2
import glob
from PIL import Image
import numpy as np
import skimage
import scipy
import pygame
import os
import matplotlib.pyplot as plt
from stacking import stack_images


class GeometryDetectionMedicalImages:
    def __init__(self):
        self.source_path = r"code_and_pictures/mri_testing_images/" # "MRI_SCREENSHOTS/PATIENT_1/"  #"mri_images/"
        self.iterations = int
        self.image_list = []
        self.pil_to_numpy_list = []
        self.gray_image_list = []
        self.blur_image_list = []
        self.threshold_image_list = []
        self.contours_value_list = []
        self.hierarchy_value_list = []
        self.big_contour_value_list = []
        self.mask_list = []
        self.mask_with_gray_image_list = []
        self.area_list = []
        self.fill_in_image_list = []
        self.draw_contour_image_list = []
        self.screen_size_X = int
        self.screen_size_Y = int
        self.image_coordinates_X = int
        self.image_coordinates_Y = int

    def run_yolo_model_automatic(self):
        '''
        Runs the yolo v5 model set automatically using the os.sys

        :return: N/A
        '''
        # How many iterations the yolo model will run
        self.iterations = 2

        # Calling the terminal to make the yolo model automatic
        os.sys(f"python train.py --img 640 --batch 8 --epochs {self.iterations} --data bvr.yaml --weights yolov5s.pt "
               f"--cache")

    def image_folder_list(self) -> Image:
        """
        Opening a folder containing images that will be stored in a list

        :return: a list of images
        """
        # Calling the image folder and storing in a list
        for filename in glob.iglob(f'{self.source_path}/*'):
            # Opens the current image
            call_image = Image.open(filename)

            # Stores image in a list
            self.image_list.append(call_image)

        return self.image_list

    def image_conversion_data_type(self, image_list: Image) -> list:
        """
        The image_list is in PIL.Image.image that needs to be converted to numpy array

        :return: converted data type image list
        """
        # Initializing the construct value
        self.image_list = image_list

        # Converting "PIL.Image.image" to an "numpy array"
        for image in self.image_list:
            # Converting the image type
            numpy_image = np.array(image)

            # Storing the image in a list
            self.pil_to_numpy_list.append(numpy_image)

        return self.pil_to_numpy_list

    def gray_scale(self, pil_to_numpy_list: np.ndarray) -> list:
        """
        Converts an image to gray scale

        :return: gray scale image list
        """
        # Initializing the constructor value
        self.pil_to_numpy_list = pil_to_numpy_list

        # Creating a for loop for every image from the list
        for image in self.pil_to_numpy_list:
            # Applying gray scale to the image
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Storing the gray image to a list
            self.gray_image_list.append(gray_image)

        return self.gray_image_list

    def blur_image(self, gray_image_list: np.ndarray) -> list:
        """
        Blurs the image to get rid of any bright small pixels on an image

        :return: list of blur image
        """
        # Initializing the constructor value
        self.gray_image_list = gray_image_list

        # Creating a for loop for every image from the list
        for image in self.gray_image_list:
            # Using a Gaussian blur to blur the image
            blur_image = cv2.GaussianBlur(image, (5, 5), 0)

            # Storing the blur image in a list
            self.blur_image_list.append(blur_image)

        return self.blur_image_list

    def get_threshold(self, blur_image_list: np.ndarray) -> list:
        """
        Using the gray scale images to find the threshold of each image

        :return: list of threshold image values
        """
        # Initializing the constructor value
        self.blur_image_list = blur_image_list

        # Creating a for loop for every image from the list
        for image in self.blur_image_list:
            # Creating a threshold on the image (inverted colors (black and white))
            ret, threshold = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)

            # Storing the threshold image in a list
            self.threshold_image_list.append(threshold)

        return self.threshold_image_list

    def find_contours(self, threshold_image_list: np.ndarray) -> list:
        """
        Finds the contours of each image and stores the contour in an array. The contour will store the coordinates
        of the contours

        :return: list of contours image values
        """
        # Initializing constructor value
        self.threshold_image_list = threshold_image_list

        # Creating a for loop for every image from the list
        for image in self.threshold_image_list:
            # Find contours (skimage.measure.find_contours returns a list need to convert to np)
            contours = skimage.measure.find_contours(image, 0.8)

            # Find contours (openCV method to find contours)
            contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Storing the contours list
            self.contours_value_list.append(contours)

            # Storing the hierarchy list
            self.hierarchy_value_list = hierarchy

        return self.contours_value_list, self.hierarchy_value_list

    def get_big_contours(self, contours_value_list: np.ndarray) -> Tuple[list, list]:
        """
        Inputs the contour list then convert the contour coordinates to area. Then store the big contour values

        :return: big contours value image list
        """
        # Initializing the constructor value
        self.contours_value_list = contours_value_list

        # For loop calls for all images
        for i in range(len(self.threshold_image_list)):
            # Creating a temp list for indentation purposes for the contours may be correlated for its specific image
            new_contour_indentation_temp_list = []

            # for loop gets the contours for the specific image being called
            for j in range(len(self.contours_value_list[i])):
                # Creating a temp variable for the iteration
                temp_contour = self.contours_value_list[i][j]

                # Creating a temp variable that will expand the dimension array that is float32 (skimage contours)
                temp_expand_array = np.expand_dims(temp_contour.astype(np.float32), 1)

                # Using a temp variable to convert float32 to UMat (skimage contours)
                temp_umat_conversion = cv2.UMat(temp_expand_array)

                # Getting the contour area from the temp variable
                area = cv2.contourArea(temp_contour)

                # Creating an if statement for storing the big contours only (skimage > 15) (openCV > 2000)
                if area > 2000:
                    # Storing the big contour in a list
                    new_contour_indentation_temp_list.append(temp_contour)
                    self.area_list.append(area)
                else:
                    # Creating an empty array of zeros to eliminate the small contours
                    black_pixels = np.zeros_like(temp_contour)

                    # Multiplying a black image times the contour (output is nothing)
                    small_mask = black_pixels * temp_contour

                    # Storing the small contour in a list
                    new_contour_indentation_temp_list.append(small_mask)

            # As each iteration ends then add the temp_list to the new contour list
            self.big_contour_value_list.append(new_contour_indentation_temp_list)

        return self.area_list, self.big_contour_value_list

    def create_mask(self, threshold_image_list: np.ndarray, gray_image_list: np.ndarray,
                    pil_to_numpy_img_list: np.ndarray):
        '''
        Gets two image mask, the first mask is the contour image and the second mask is everything is noisy but the
        contours (image mostly white)

        :param threshold_image_list: threshold image list
        :param gray_image_list: gray image list
        :param pil_to_numpy_img_list: RGB image list
        :return: two mask image list
        '''
        # Initializing the constructors values
        self.threshold_image_list = threshold_image_list
        self.gray_image_list = gray_image_list
        self.pil_to_numpy_list = pil_to_numpy_img_list

        # Creating a for loop to iterate each threshold
        for image_one, image_two in zip(self.threshold_image_list, self.gray_image_list):
            # Applying the bitwise function (raw mask image since there are mix values)
            mask_image = cv2.bitwise_and(image_one, image_two)

            # Storing the mask to the list
            self.mask_list.append(mask_image)

        for image_one, image_two in zip(self.threshold_image_list, self.pil_to_numpy_list):
            # Keep values only that are very white
            gray_mask_image = cv2.bitwise_not(image_two, image_one)

            # Storing the inverted mask to the list
            self.mask_with_gray_image_list.append(gray_mask_image)

        return self.mask_list, self.mask_with_gray_image_list


    def fill_in_image_holes(self) -> list:
        """
        Inputs the threshold image and fill in the gaps

        :return: filled in image list
        """
        # For loop for calling the image
        for i in range(len(self.threshold_image_list)):
            # Fill in the contours empty gap
            self.fill_in_image_list = scipy.ndimage.binary_fill_holes(self.threshold_image_list[i])

        return self.fill_in_image_list

    def eliminate_white_small_pixels(self):
        for image in self.threshold_image_list:
            one_matrix_image = np.ones_like(image)
            print("The counter is at: ", image)
            print(one_matrix_image)

    def insert_and_gather_ellipse_data(self, image_list: np.ndarray, contour_value_list: list):
        # Creating a empty variable for the index 
        temp_image = None
        print(f"The length of the contours is: {len(contour_value_list)}")

        # Create another for loop iterate every image
        for image in image_list:
            # Creating a blank image (copying the image itself)
            blank_image = image.copy()
            print(blank_image.shape)

            # Calling a for loop to iterate each contour from the image
            for index in contour_value_list:
                # Draw the contour onto the image
                temp_image = cv2.drawContours(blank_image, index, 0, (0, 255, 0), 3)

                # Creating an ellipse or the best ellipse
                print(type(temp_image))
                ellipse = cv2.fitEllipse(temp_image)
                print(type(ellipse))

                # Separate the ellipse information
                center_coordinate, semi_axis, rotational_angle = ellipse

                # Print the ellipse information
                print("==========================================================")
                print(f"The X coordinate of the center: {center_coordinate[0]}")
                print(f"The Y coordinate of the center: {center_coordinate[1]}")
                print(f"The major semi-axis (Diameter): {semi_axis[0]}")
                print(f"The minor semi-axis (Diameter): {semi_axis[1]}")
                print(f"The rotational angle (Degrees): {rotational_angle}")
                print("==========================================================")

                # Creating the image (something we can see)
                temp_image = cv2.ellipse(blank_image, ellipse, (0, 0, 255), 4, cv2.LINE_AA)

            cv2.imshow('ellipse', temp_image)
            cv2.waitKey(0)

    def send_data_to_freecad(self):
        pass

    def image_information(self, image_list: np.ndarray):
        '''
        Checks the width, height, and channels of each image

        :param image_list: an image
        :return: N/A
        '''
        # Iterating every image
        for image in image_list:
            # Checking the shape of each image (width, height, channel)
            width, height, channels = image.shape

            # Printing the information
            print(f"The width is: {width}, the height is: {height}, and the amount of channels are: {channels}")

    def extract_image_matrix_information(self, image_list: np.ndarray):
        '''
        Allow the print function to display the entire matrix dataset to be displayed

        :param image_list: an image
        :return: N/A
        '''
        # Iterating every image
        for image in image_list:
            # Allowing the numpy array to display the entire dataset
            np.set_printoptions(threshold=np.inf)

            # Printing the matrix (the image) and checking the values
            print(image)

    def plot_images_and_contours(self, image_list: np.ndarray, contour_value_list: np.ndarray):
        '''
        New plot image function, currently not working with two images but runs extremely fast compare to plt.imshow

        :param image_list:
        :param contour_value_list:
        :return: N/A
        '''
        # Set screen width and height size
        self.screen_size_X = 650
        self.screen_size_Y = 400

        # Set coordinates for the image
        self.image_coordinates_X = 0
        self.image_coordinates_Y = 0

        # Initializing the screen window size
        screen = pygame.display.set_mode((self.screen_size_X, self.screen_size_Y))

        # Window name
        pygame.display.set_caption('Arty-Chan Window Display')

        # Temp solution to see if the code works or not
        temp_image = "mri_images/patient1G.png"

        # Create a surface object to be drawn on the pygame application
        image_display = pygame.image.load(temp_image).convert()

        # Block Transfer (blit) is copy the content to another surface
        screen.blit(image_display, (self.image_coordinates_X, self.image_coordinates_Y))

        # Will update the content of the entire display
        pygame.display.flip()

        # Switch button to pressing the close button
        stop_program_button = False

        # A while loop for the user to quit with a button
        while not stop_program_button:
            # For loop for wait for a buttons or actions to be pressed
            for event in pygame.event.get():
                # When closing the button is true then break the while loop
                if event.type == pygame.QUIT:
                    # Make the switch button true
                    stop_program_button = True

        # Quit the application
        pygame.quit()

    def call_image_and_contours(self, threshold_image_list: list, contour_value_list: list):
        """
        Drawing the contour to its correlated image. WORKS WITH ONLY SKIMAGE CONTOUR NOT OPENCV CONTOUR

        :param threshold_image_list: a list of images that have been threshold
        :param contour_value_list: a list of contour values to draw the contour line
        """
        # Initializing the constructor values
        self.threshold_image_list = threshold_image_list
        self.big_contour_value_list = contour_value_list

        print(len(threshold_image_list))
        print(len(contour_value_list))

        # Calls the image list from each index draw the contours
        for i in range(len(self.threshold_image_list)):
            fig, ax = plt.subplots()
            ax.imshow(self.threshold_image_list[i], cmap=plt.cm.gray)
            plt.title("Image")
            for contour in self.big_contour_value_list[i]:
                ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
            plt.show()

        # Close all images
        plt.close('all')

    def draw_contours(self, threshold_image_list: list, contour_value_list: list):
        """
        This method is to draw contours ONLY if you are using OPENCV library

        :param threshold_image_list: a list of images that have been threshold
        :param contour_value_list: a list of contour values to draw the contour line
        :return: N/A
        """
        # Initializing the constructor values
        self.threshold_image_list = threshold_image_list
        self.big_contour_value_list = contour_value_list

        # Calls the image list from each index draw the contours
        for image in self.threshold_image_list:
            # Call all the contours but iterate it as an integer (to load all the contours at once to the function)
            for index_cnt in self.big_contour_value_list:
                # For the current image, draw the contour
                image = cv2.drawContours(image, contours=index_cnt, contourIdx=-1, color=(0, 255, 0), thickness=3)

            # Add updated image to the list
            self.draw_contour_image_list.append(image)

        # Displaying the image
        print(len(self.draw_contour_image_list))
        cv2.imshow("An image", self.draw_contour_image_list[0])
        cv2.waitKey(0)

    def run_all_functions(self):
        """
        Runs all the function in the class

        :return: N/A
        """
        # Get the list of images
        img_list = self.image_folder_list()
        print(self.source_path)
        print(f"The total amount of images is: {len(img_list)}")

        # Convert PIL to numpy format per image
        pil_to_numpy_img_list = self.image_conversion_data_type(img_list)
        
        # Grayscale the image
        gray_img_list = self.gray_scale(pil_to_numpy_img_list)

        # Gaussian blur image
        blur_img_list = self.blur_image(gray_img_list)

        # Gets the threshold from the image
        threshold_img_list = self.get_threshold(blur_img_list)

        # Get the contour list
        contour_val_list, hierarchy_val_list = self.find_contours(threshold_img_list)

        # Filter Contours (Big Contours)
        contour_area_list, big_contour_val_list = self.get_big_contours(contour_val_list)

        # This comment is causing issues (need to look into )
        # self.draw_contours(threshold_img_list, big_contour_val_list)

        # self.insert_and_gather_ellipse_data(threshold_img_list, big_contour_val_list)




