# Disclaimer
All patient images have been removed for privacy. Only one representative image is displayed.

# Objective of the Project
3D Geometry Reconstruction of Medial Images 

Client: Biomedical Soft Tissue and Implants Modeling Upscale (BioTim-Us) 

Advisor: Mathias Brieu, Ph.D 

Students: Stephanie Reyes, Sarahi Munoz, Christopher Morales, Paul Bahena 


This project focused on using numerical tools to analyze medical images and construct a 3D model of the organs present in the image. The goal was to provide a detailed 3D model that could be easily manipulated for use in the medical field. The focus was on Magnetic Resonance Images (MRI) of the pelvic anatomy of women patients, with an emphasis on three main organs, the bladder, vagina, and rectum. To construct the 3D models from the MRI scans computer vision was utilized as the main tool for image analysis. An object detection tool was developed and trained to detect, differentiate, and label the bladder, vagina, and rectum. These same images were converted to a greyscale, which allowed the organs of interest to be isolated as well as identified by drawing contours around them. An ellipse was then fitted into each contour, and from these ellipses certain parameters could be obtained. Including the center point (x, y, z), the length (l), height (h) and orientation (n). This data can then be utilized to create a 3D CAD model of the patients’ pelvic organs.  

All numerical tools developed are based on open-source software (python, open-CV, makense.ai, yolo, and FreeCAD). 



# Installing Programs 

For this section we are going to install the mandatory applications for the project. For the IDE's you have mutiple options what to choose from and the different type of git's. The **NECESSARY** application you need to insall are: Slicer, FreeCAD, an IDE, and a Git. 

You may ask what is Git? A git where a group of team can push any code/file to the cloud where everybody can pull or push the data. Pull means downloading the latest code while push means send the updated file/code to the cloud. Where any modifications that are made to a file/code everybody will get the latest file/code. Each time you pull/push, what you are actually doing is called a commit. Where every commit is store where everybody can see the modifications that have been done to the project. Why did you recommend so many Git's? We recommended a various types of Git's due to personal preference or some applications are better for performance.

Why are you given multiple options for IDE? Well it really depends on the person preference or limited to application due to operating system. Each IDE have there own benefits and downsides, the only thing you need to install for any IDE is **mambaforge** and change the conda environment from python to conda *(mambaforge)*

Why did you use 7zip for archiving each version? 7zip is useful and simple to use and give more options to install more programs/libraries that we may need in the future. Overall, nice tool to know and learn.



### Slicer 

An applications we are going to need is [Slicer](https://www.slicer.org), that is open source and uses python interpreter. From teams, you are going to need to download the zip folder that has the MRI data. With this data, the Slicer will convert the data into each plane to the respect of time that will be used for python (computer vision part of the project). Once you installed Slicer, you need to install a library when using the application. When you open the Slicer application, go to *Extension Manager*, find the library called ***slicerDMRI*** and you will have everything you need. 


### FreeCAD 
An application we are going to need is [FreeCAD](https://www.freecadweb.org), that is open source and uses python interpreter. For FreeCAD we are going to create a 3D model from using the data we get from the computer vision aspect and simulate a model using the data in FreeCAD.



### IDE 
An Integrated Developer Environment (IDE) is a software application that helps prgorammers develop programs. For our project you will be given an option which IDE you like to use, just note sometimes/rarely some IDE's will make a code work or some will not run the same code due to what plug-ins the IDE used. It is better for everyone to use the same IDE but we understand some uses other operating system. *Pick one IDE you will like to use*

- [PyCharm Professional](https://www.jetbrains.com/pycharm/download/#section=windows)
  - *NOTE: PyCharm is a paid IDE but for students or teachers it is free if you use the link down below. When setting up PyCharm Professional it will ask you to sign in to use the program.*
    - [PyCharm Professional License for Students/Teachers](https://www.jetbrains.com/shop/eform/students)
- [Visual Studios](https://visualstudio.microsoft.com/downloads/)
- [Atom](https://atom.io)
- [Sublime Text](https://www.sublimetext.com/3)
- [Spyder IDE](https://www.spyder-ide.org)
- [Vim](https://www.vim.org) 



### Miniforge *(Conda Environment for IDE)*
After installing an IDE, we are going to use [Miniforge](https://github.com/conda-forge/miniforge) for PyCharm. Its a distrobution of python that is lighly package and have the avaibility  In the website find, **mambaforge** and run the software then a prompt will show up. It will ask the user to check mark some boxes and check mark the following: ***Create a start menu shortcut***, ***Register Mambaforge as my default Python 3.\#***, and ***Clear the package cache upon completion***. *NOTE: Do not install mambaforge but install mambaforge due to updating to the lastest conda is easier*



### Git
Git is a distributed revision control system that is generally used for source code management in software development. Git is used to tracking changes in the source code. The distributed version control tool is used for source code management. For this project you are going to need to pick one Git that you may like to use. All Git's are the same but approach it in a different way and pick one that you may like to use. 

- [Git Bash](https://git-scm.com/downloads)
- [Github Desktop](https://desktop.github.com)
- [GitKraken](https://www.gitkraken.com)
- [SourceTree](https://www.sourcetreeapp.com)
- [Aurees](https://aurees.com)
- [Git Cola](https://git-cola.github.io)
- [Fork](https://dev.to/theme_selection/best-git-gui-clients-for-developers-5023)



### File Archiver
- [7zip](https://www.7-zip.org)



### Outside Source 
- [Virtual Makerspace](https://calstatela.instructure.com/enroll/K3NH8X) 



# Setting up PyCharm Professional and Miniforge

### MINIFORGE/MAMBAFORGE DEFAULT PATH

Windows Default Path for Miniforge/Mambaforge: C:\Users\YOURCOMPUTERNAME\miniforge3\python.exe

The default path for miniforge for WINDOWS Operating System

### To make the CONDA ENVIRONMENT work on any IDE:
You may have some issues making the conda path work on a WINDOWS OS. All you need to do is open the  **Miniforge Prompt Application** and type in the following:

```bash
conda init powershell
```

Close the application, and this will resolve a lot of conda directory path not being read. [SOURCE](https://stackoverflow.com/questions/54828713/working-with-anaconda-in-visual-studio-code)

### Installing Libraries to Miniforge
Since Miniforge is very lightly packed with libraries we need to install some libraries. Go to your computer and on the search bar, type in Miniforge and open the program. Once you have open the program, the application will look like a terminal base application. All you need to do is type in the following one by one on the terminal are:
- pip install opencv-python
- pip install matplotlib
- pip install imutils
- pip install scikit-image
- pip install random2
- pip install Pillow
- pip install glob2
- pip install ushlex
- pip install pyautogui
- pip install scipy
- pip install PyQt6
- pip install pygame
- pip install slicer

### Setting Miniforge as your conda for PyCharm Professional 
Download the current project and open it on PyCharm and once open go to *File* > *Settings*, *Project: main.py* and ***click on Python Interpreter***. As the figure down below will show, 

![PyCharm Setting Menu](https://user-images.githubusercontent.com/54751574/190874372-da39224e-c4e0-4f40-80e6-e0617ef2a19b.png)

Then click on the on the Python Interpreter list and click **show all**

![Python Interpreter List](https://user-images.githubusercontent.com/54751574/190874455-059b4f0b-9d7c-4af9-bf2c-50c26e557028.png)

Another window will prompt up and we need to find the directory for miniforge. Click on the **+**, 
*NOTE: For my computer my directory is C:\User\artor\miniforge3\python.exe*
*NOTE: The directory could be the same for you or not. You could click on the program and ask for its directory*

![Miniforge Conda Directory Setup](https://user-images.githubusercontent.com/54751574/190874618-320065a6-c8ac-461e-af52-7c6f0aef18ea.png)

Now we have found our specific conda environment for the project, press **ok**, and make sure miniforge is selected on the Python Interpreter list. Once you have clicked **ok** again, you should be able to start coding. 
To be sure that you have use the correct conda, you should have no error or red underline on ***import cv2***.
![Importing Libraries working and no error](https://user-images.githubusercontent.com/54751574/190874712-92cf6088-0c3d-4b1a-a2d2-3a00b659183d.png)




[Helpful link for learning Github Readme Setup](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

# Anaconda Python Interpreter

If you installed Anaconda or miniconda instead of miniforge then do the following to determine you conda path.

```python
which python
```
This will work for mac. All you need to do is do the following as the miniforge conda setup for the IDE. 


# FreeCAD Interpreter (THIS IS VERY IMPORTANT, PLEASE READ)
Despite installing miniforge/mambaforge/miniconda, we will have to use the FreeCAD Python interpreter to use the **FreeCAD Library**. If you did not change the directory of the FreeCAD then it should be the following: 


```bash
C:\Program Files\FreeCAD 0.20\bin\python.exe
```

### Important facts using different libraries
![image](https://user-images.githubusercontent.com/54751574/194931088-1d31546b-519b-4963-876e-55fb7953101d.png)
- One library uses one method while another uses a different


# Here is what you need to know crash course:


- [Link for crash course](https://scikit-image.org/docs/dev/user_guide/numpy_images.html)
- [Link for Colors and Hue](https://stackoverflow.com/questions/26244539/open-cv2-python-multiply-images)
- [Link for another crash course](http://simplecv.org)
- [Link for CV2 to Skimage or Skimage to CV2 image conversion](https://scikit-image.org/docs/stable/user_guide/data_types.html#working-with-opencv)
- [Link for learning what is Git](https://www.atlassian.com/git/tutorials/what-is-git)
- [Link for Python Crash Course](https://ehmatthes.github.io/pcc/)
- [YouTube Link for Python Crash Course](https://youtu.be/XKHEtdqhLK8)
- [Link for Crash Course or General Idea of Computer Vision](https://opencv.org/opencv-free-course/)
- [Link for Blob Modifications/Detections](https://learnopencv.com/blob-detection-using-opencv-python-c/)
- [Link for best library methods](https://neptune.ai/blog/image-processing-python-libraries-for-machine-learning)
- [Link for sys.argv](https://docs.python.org/3/library/sys.html?highlight=sys#sys.argv)
- [Link for tutorials for PyQt6 Application Contruction](https://doc.qt.io/qtforpython/tutorials/index.html)
- [Link for PyQt6 vs PySide6](https://www.pythonguis.com/faq/pyqt6-vs-pyside6/)
- [Link to learn Tkinter](https://www.geeksforgeeks.org/python-tkinter-tutorial/)



### API Reference for Libraries
- [PyQt6](https://doc.qt.io/qtforpython/api.html)
- [Numpy](https://numpy.org/doc/stable/reference/)
- [matplotlib](https://matplotlib.org/stable/api/index.html)
- [scipy](https://docs.scipy.org/doc/scipy/reference/)
- [opencv](https://docs.opencv.org/4.x/)
- [skimage](https://scikit-image.org/docs/stable/api/api.html)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [OS](https://docs.python.org/3/library/os.html)
- [glob](https://docs.python.org/3/library/glob.html)
- [imutils](https://github.com/PyImageSearch/imutils)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [FreeCAD](https://wiki.freecadweb.org/FreeCAD_API)
- [Slicer](https://slicer.readthedocs.io/en/latest/developer_guide/api.html)
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
- [threading](https://docs.python.org/3/library/threading.html)
- [Tkinter](https://docs.python.org/3/library/tk.html)



# Updates Information

- 11/18/2022
  - BIG UPDATE: We are going to change the code where we are going to use PyCharm  that will send a command line to find the ideal images that will be cropped and saved as an png extension. Where the PyCharm IDE will do the appropiate computer vision methods to find an contour. After finding the contours, we will determine the ellipse of the contour that will be sent to FreeCAD API to create a model. 

- 10/29/2022
  - Check in the discussions about the major issue for version 2. In the discussion there will be images and methods on how to fix it. Anyways, the current issue we are having is one of the constructures is not saving the value which is causing a lot of issue. We only know about this due to a tool that PyCharm has called Debugging Tool. The debugging tool is useful to see whats inside a variable (the raw data).

- 10/28/2022
  - Version 2 of the code will be uploaded soon and almost completed. It works but adding doc string to the new structure of the code. Just implemented the PyQt6 code and its very basic on creating a simple application. Please note, do not update ay packages of this moment in mambaforge due to some of the newest libraries is affecting other libraries. 

- 10/25/2022 
  - For matplotlib, do not use the latest package update. We have to go back to ***pip install matplotlib==3.5.0***, with this the code will work. I have decided (arty-chan) to implement a GUI for the code due to deteriming better contour values or let the user decide whether the data is good or not. The code has been optimized to the max and currently implementing a more sophisticated code such as SELF. Hopefully, in the near future with some research, we could implement C++ and bash script to the code to make it run faster and splitting the image into chunks for each core. 

- 10/11/2022
  - Added multiple resources regarding about the topic of Computer Vision, Slicer API, FreeCAD API, and every library reference API. The API for every library will tell you the inputs/outputs and tells you the type it needs or sends out. The library reference API will tell you its overall and sometimes an example what does the function does. Furthermore, their are multiple links for crash courses to keep everyone update or how a new member can tag along. 

- 10/7/2022
  - We finally are almost done with version 1.1V where the code will be able to detect contour area and filter the small contours. We needed to filter the small contours since we are going to apply an ellipse onto the contour. Where we are still deciding whether the ellipse should be inside the contour while losing some precious data or the ellipse so gather the ellipse in whole while gatting useless data. Furthermore, we are using the contour area to label and creating a mask for every image. Finally, we have coded a cube using FreeCAD Python Console and understand what FreeCAD commands are. We are planning to start the API for FreeCAD and in another version we will send the ellipse data onto FreeCAD. Finally, we are are still figuring out how to make the small contour "black" for the masking image processes. 

- 09/24/2022
  - We finally got python to open Slicer using OS. We are going to experiment with other libraries to determine whether if it is possible for us to use python to control multiple applications, getting data from Slicer to send data to FreeCAD while using an IDE for everything. 

- 09/23/2022
  - The code is able to detect any contours from any image however it detects the tiny contours and need to filter it out. As of now, version one is completed since the main purpose of the code is to detect contours from the mri images. Next step of the code is determine the area and parameter of each contour to filter out the smal contour. Then draw an ellipse and label each contour. 

- 09/18/2022
  - Currently the model has a functioning code that can determine the threshold and contours of a tissue however it is not using ellipse rather than the outline of the tissue. Another note, is creating the mask line seems to be difficult due to the contours draw lines are saved in a list that will be used in another function. Yet, we haave trouble trying to redraw the lines or make a line for other images. 


- 09/16/2022
  - The current code depends on a folder filled with images that will be store in a list. The list will have the option to be resize (upscale/downscale),
futhermore, the code will conduct converting the images to numpy array, gray scale all images, and getting the images threshold. 


# Acknowledgement 

We used an artificial intelligence system named YOLO that not only identified the green, yellow, and pink images but also annotated and produced descriptive labels for the images.We would like to thank YOLO for providing the documentation, implementation, and the use of YOLO.
