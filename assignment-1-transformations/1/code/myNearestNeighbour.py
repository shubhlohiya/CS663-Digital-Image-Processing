import numpy as np
import matplotlib.pyplot as plt

def myNearestNeighbour(image):
    """ 
        Function to enlarge image using Nearest Neighbout interpolation
        Input: Image of size MxN
        Output: Image of size (3M-2)x(2N-1)        
    """
    
    h1, w1 = image.shape # original image width and height
    h2, w2 = 3*h1-2, 2*w1-1 # target width and height
    
    # create empty array of enlarged size to store the interpolated image
    res = np.empty((h2, w2), dtype=int) 
    
    # calculate width ratios
    xratio = w1/w2
    yratio = h1/h2
    
    # find nearest-neighbour values for every pixel from corresponding area in original image
    for i in range(h2):
        for j in range(w2):
            y = min(round(i*yratio), h1-1)
            x = min(round(j*xratio), w1-1)
            res[i,j] = image[y, x]
    
    plt.imshow(res, cmap='gray', vmin=0, vmax=255)
    plt.colorbar()
    plt.title("Nearest Neighbour Interpolation - Barbara\n")
    plt.show()
    
    return res