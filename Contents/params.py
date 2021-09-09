import numpy as np

# limits for gray scale

limit_up = 255
limit_down = 0

# list of images filepath

list_of_files = [
    'Images/office_1.jpg', 'Images/office_2.jpg', 'Images/office_3.jpg', 
    'Images/office_4.jpg', 'Images/office_5.jpg', 'Images/office_6.jpg']

# list of images exposures

exposures = np.array([1./30., 1./10., 1./3., .625, 1.3, 4])

# filepath for curve calibration

filepath_curve_calibration = "curve.m"

# Values for gamma correction

gamma = 1./2.2