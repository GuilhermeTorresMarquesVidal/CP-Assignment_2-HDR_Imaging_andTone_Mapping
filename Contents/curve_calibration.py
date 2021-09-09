import numpy as np

def read_curve_calibration(filepath):

    text = ''

    with open(filepath,"r") as f:
        text = f.read()
        f.close()
        
    return text

def curve_calibration_to_narray(text):

    lines = text.split('\n')

    R = []
    G = []
    B = []

    for line in lines[1:-1]:
        channels = line.split()
        R.append(float(channels[0]))
        G.append(float(channels[1]))
        B.append(float(channels[2]))
    
    R = np.array(R)
    G = np.array(G)
    B = np.array(B)

    calibration_curve = np.zeros((len(R),3))

    calibration_curve[:,0] = R
    calibration_curve[:,1] = G
    calibration_curve[:,2] = B

    return calibration_curve

def get_curve_calibration(filepath):

    text = read_curve_calibration(filepath = filepath)
    calibration_curve = curve_calibration_to_narray(text = text)

    return calibration_curve