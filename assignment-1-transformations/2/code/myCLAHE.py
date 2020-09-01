import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import ceil


def get_cdf(pixel, image, shape, half_window_size, threshold):
    
    left = max(pixel[1] - half_window_size, 0)
    right = min(pixel[1] + half_window_size , shape[1])
    top = max(pixel[0]-half_window_size+1, 0)
    bottom = min(pixel[0]+half_window_size, shape[0])
    
    
    subset = image[top:bottom, left:right]
    
    shape1 = subset.shape
    hist = np.array([0.0 for i in range(256)])
    for i in range(shape1[0]):
        for j in range(shape1[1]):
            hist[subset[i,j]]+=1

    hist /= shape1[0]*shape1[1]


    clipped_area = 0.0
    for i in range(256):
        p = hist[i] - threshold
        if p > 0:
            hist[i] = threshold
            clipped_area += p
    hist += clipped_area/256
    
    s = 0.0
    cdf = np.empty(256)
    for i in range(256):
        s+=hist[i]
        cdf[i] = s
    return cdf


def clahe(image, window_size = 101, clip_threshold = 0.01):
    shape = image.shape
    half_window_size = window_size//2
    m = ceil(shape[0]/window_size)
    n = ceil(shape[1]/window_size)
    lookup = np.zeros((m+2, n+2, 256))
    
    for i in range(m):
        for j in range(n):
            pixel = (min(i*window_size + half_window_size, shape[0]-1), min(j*window_size + half_window_size, shape[1]-1))
            lookup[i+1][j+1] = get_cdf(pixel, image, shape, half_window_size, clip_threshold)
            
    
    res = np.empty(shape, dtype=int)

    for i in range(shape[0]):
        for j in range(shape[1]):
            
            val = image[i, j]
            
            topleft = ((i-half_window_size)//window_size + 1, (j-half_window_size)//window_size + 1)
            topright = (topleft[0], topleft[1]+1)
            bottomleft = (topleft[0]+1, topleft[1])
            bottomright = (topleft[0]+1, topleft[1]+1)
            
            # windowcentres
            if (i-half_window_size)%window_size ==0 and (j-half_window_size)%window_size==0:
                res[i,j] = int(lookup[topleft][val]*255)
                continue
            
            # Check borders and corners
            A = topleft[0] in [0, m]
            B = topleft[1] in [0, n]
            
            a = 1 - (i - (topleft[0]-1)*window_size - half_window_size+1)/window_size
            b = 1 - (j - (topleft[1]-1)*window_size - half_window_size+1)/window_size
            
            if not (a<=1 and a >=0):
            	print("WRONG", a , b)
            	break 
            # corners
            if A and B:
                a = 0 if topleft[0]==0 else 1
                b = 0 if topleft[1]==0 else 1
                
            # borders
            elif A!=B:                
                    
                if topleft[0] == 0:
                    a = 0
                elif topleft[0] == m:
                    a = 1
                elif topleft[1] == 0:
                    b = 0
                elif topleft[1] == n:
                    b = 1                
            
            #interpolate
            res[i, j] = int((a*(b*lookup[topleft][val] + (1-b)*lookup[topright][val]) 
                + (1-a)*(b*lookup[bottomleft][val] + (1-b)*lookup[bottomright][val]))*255)
            
    return res







image = cv2.imread(r"../data/barbara.png", cv2.IMREAD_GRAYSCALE)
res = clahe(image, 50 , 0.01)
cv2.imshow("ImageWindow 50", res.astype(np.uint8))


res = clahe(image, 250 , 0.01)
cv2.imshow("ImageWindow 250", res.astype(np.uint8))

res = clahe(image, 10 , 0.01)
cv2.imshow("ImageWindow 10", res.astype(np.uint8))

cv2.waitKey(0)


#FOR RBG
# res = np.array(list(map(clahe, image)))


