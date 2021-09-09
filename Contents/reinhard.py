import numpy as np

def reinhard_operator(image):

    gamma = 1.0

    L = .299*image[:,:,0] + .587*image[:,:,1] + .114*image[:,:,2]

    s = L.shape

    n = s[0]*s[1]

    Ln = np.exp(np.sum(np.log(L + gamma))/n)

    alpha = 0.18

    Ls =  (alpha/Ln)*image

    Lg = Ls/(1+Ls)

    return Lg