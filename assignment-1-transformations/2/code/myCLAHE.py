import numpy as np
from math import ceil
import matplotlib.pyplot as plt
import cv2

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


def clahe(image, window_size = 51, clip_threshold = 0.01):
    shape = image.shape
    half_window_size = window_size//2
    m = ceil(shape[0]/window_size)
    n = ceil(shape[1]/window_size)
    lookup = np.zeros((m+2, n+2, 256))
    
    for i in range(m):
        for j in range(n):
            pixel = (min(i*window_size + half_window_size, shape[0]-1), 
            	min(j*window_size + half_window_size, shape[1]-1))
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
            
            # bilinear interpolation
            res[i, j] = int((a*(b*lookup[topleft][val] + (1-b)*lookup[topright][val]) 
                + (1-a)*(b*lookup[bottomleft][val] + (1-b)*lookup[bottomright][val]))*255)
            
    return res


def myCLAHE(image, name):
	
	if(len(image.shape)==3):

		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		fig1, ax1 = plt.subplots(1, 2, figsize=(100, 100))

		im = ax1[0].imshow(image)
		ax1[0].title.set_text(f"{name} - original")

		res = np.array(list(map(clahe, image, [50]*len(image) , [0.01]*len(image))))
		im = ax1[1].imshow(res)
		ax1[1].title.set_text(f"{name} - window size: 50, \nclip threshold: 0.01")

		fig1.colorbar(im, ax=ax1.ravel().tolist())


		fig1a, ax1a = plt.subplots(1, 2, figsize=(100, 100))

		res = np.array(list(map(clahe, image, [250]*len(image) , [0.01]*len(image))))
		im = ax1a[0].imshow(res)
		ax1a[0].title.set_text(f"{name} - window size: 250, \nclip threshold: 0.01")

		res = np.array(list(map(clahe, image, [10]*len(image) , [0.01]*len(image))))
		im = ax1a[1].imshow(res)
		ax1a[1].title.set_text(f"{name} - window size: 10, \nclip threshold: 0.01")

		fig1a.colorbar(im, ax=ax1a.ravel().tolist())


		fig1b, ax1b = plt.subplots(1, 1, figsize=(100, 100))
		res = np.array(list(map(clahe, image, [50]*len(image) , [0.005]*len(image))))
		im = ax1b.imshow(res)
		ax1b.title.set_text(f"{name} - window size: 50, \nclip threshold: 0.005 (halved)")

		fig1b.colorbar(im, ax=ax1b)


	else:

		fig1, ax1 = plt.subplots(1, 2, figsize=(100, 100))

		im = ax1[0].imshow(image, cmap='gray', vmin=0, vmax=255)
		ax1[0].title.set_text(f"{name} - original")

		res = clahe(image, 50 , 0.01)
		im = ax1[1].imshow(res, cmap='gray', vmin=0, vmax=255)
		ax1[1].title.set_text(f"{name} - window size: 50, \nclip threshold: 0.01")

		fig1.colorbar(im, ax=ax1.ravel().tolist())


		fig1a, ax1a = plt.subplots(1, 2, figsize=(100, 100))

		res = clahe(image, 250 , 0.01)
		im = ax1a[0].imshow(res, cmap='gray', vmin=0, vmax=255)
		ax1a[0].title.set_text(f"{name} - window size: 250, \nclip threshold: 0.01")

		res = clahe(image, 10 , 0.01)
		im = ax1a[1].imshow(res, cmap='gray', vmin=0, vmax=255)
		ax1a[1].title.set_text(f"{name} - window size: 10, \nclip threshold: 0.01")

		fig1a.colorbar(im, ax=ax1a.ravel().tolist())


		fig1b, ax1b = plt.subplots(1, 1, figsize=(100, 100))
		res = clahe(image, 50 , 0.005)
		im = ax1b.imshow(res, cmap='gray', vmin=0, vmax=255)
		ax1b.title.set_text(f"{name} - window size: 50, \nclip threshold: 0.005 (halved)")
		fig1b.colorbar(im, ax=ax1b)