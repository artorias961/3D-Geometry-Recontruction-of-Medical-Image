import sys
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
import pyqtgraph as pg


# https://www.pyqtgraph.org
def create_window():
    # Create root window
    root = Tk()

    # The title of the application
    root.title("Team 10 Application (Tkinter)")

    # Set width and height of window
    root.geometry('500x500')

    return root


def get_screen_resolutions(root):
    # Gets the height of the window screen
    height = root.winfo_screenheight()

    # Gets the width of the window screen
    width = root.winfo_screenwidth()

    # Print the information of the screen resolution
    print(f"The height is: {height}\nThe width is: {width}")


def buttons_for_application(root):
    # Creating a button for "Help" (calling the help button function)
    help_button = Button(root, text="Help", command=help_button_clicked_on)

    # Setting the position of the button
    help_button.pack(side='bottom')

    # More information about the project button
    more_info_button = Button(root, text="More Info", command=more_information_button_clicked_on)

    # Setting the position of the button
    more_info_button.pack(side='bottom')


def help_button_clicked_on():
    # Text information for help
    text = "Hello this is the 3D Geometry Reconstruction of Medical Images, this application is to help and " \
           "get an understanding of applying Computer Vision to Medical Images. Also, this mini version of the " \
           "application is to help understand how to create an application using Tkinter. Hope you enjoy this " \
           "short application demo :)."

    # Creating the popup window
    tkinter.messagebox.showinfo("Help Popup Information", text)


def more_information_button_clicked_on():
    # The text of the information
    text = "The project will do the following functions in the application\n" \
           "-> Finds the source of the image\n" \
           "-> Converts the image into gray scale (3 matrices into 1)\n" \
           "-> Apply Gaussian blur to the image (too smooth or erase small details)\n" \
           "-> Find the threshold of the image (make the image binary)\n" \
           "-> Then find the contours of the image (the outline of the threshold image)\n" \
           "-> The main project does a lot of nice stuff that will not be implemented to the application code:)\n" \
           "\n\t\tSorry!!!! -> Arty-Chan"

    # Creating a popup window
    tkinter.messagebox.showinfo("More Information about Application Processes", text)


def input_buttons_to_windows():
    pass


if __name__ == '__main__':
    root_win = create_window()
    # get_screen_resolutions(root_win)
    buttons_for_application(root_win)
    root_win.mainloop()
