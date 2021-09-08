import numpy as np

def calc_irradiance_k(image, calibration_curve):

    s = image.shape

    E = np.zeros_like(image, dtype = np.float64)

    for i in range(s[0]):
        for j in range(s[1]):
            for k in range(s[2]):
                E[i,j,k] = calibration_curve[image[i,j,k],k]

    E = np.exp(E)

    return E

def calc_irradiance(images, calibration_curve):

    n_images = len(images)

    size = list(images.values())[0].shape

    E = np.zeros((size[0], size[1], size[2], n_images))

    for index, key in zip(range(len(images)),images.keys()):
        E[:,:,:,index] = calc_irradiance_k(
            image = images[key], 
            calibration_curve = calibration_curve)

    Em = np.mean(E, axis = -1)

    return Em
