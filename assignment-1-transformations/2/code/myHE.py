import numpy as np
from PIL import Image

def nearest_int(a): #a function to find the nearest integer for a number
	if a - int(a) > 0.5:
		return int(a) + 1
	else:
		return int(a)

def Histo_equi_single_channel(image): #histogram equilization for a single channel , input is numpy array of image
    
    #frequency of occurance of each intensity initialized to zero
	freq = np.zeros((256, 1)) 
	#going through each element of array to count the number of occurance if each intensity
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			freq_val = image[i][j]
			freq[freq_val] += 1



	#frequency of occurance of a pixel inrensity in resultant image initialized to zero
	b = np.zeros((256, 1))
	#probability of picking a particular pixel from input image
	prob_one_pix = 1.0 / (image.shape[0] * image.shape[1])

	#equating CDF of a to b and scaling it with 255 as it is between (0,1)
	for i in range(256):
		for j in range(i+1):
			b[i] += freq[j] * prob_one_pix
		#rounding off to nearest integer
		b[i] = nearest_int(b[i] * 255)


	#initializing resultantat image with zeros with shape of original image
	result_img = np.zeros(image.shape)
	#updating pixel intensities of resultant images with b
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			freq_val = image[i][j]
			result_img[i][j] = b[freq_val]

	#converting numpy array to image
	result_img = Image.fromarray(result_img)
	return result_img

def histo_equilization(image):
	#converting both the images in numpt arrays
	image = np.asarray(image)
	#for grayscale image
	if len(image.shape) == 2:
		return Histo_equi_single_channel(image)
	else:
		#for color image, doing the equilization for each channel
		result_img = np.zeros(image.shape)
		for i in range(image.shape[2]):
			result_img[:,:,i] = Histo_equi_single_channel(image[:,:,i])
		result_img = Image.fromarray(result_img.astype('uint8'), 'RGB')
		return result_img


# img1 = Image.open('../data/barbara.png')
# # img1.show()
# img1_new = histo_equilization(img1)
# img1_new.show()

# img2 = Image.open('../data/TEM.png')
# # img2.show()
# img2_new = histo_equilization(img2)
# img2_new.show()

# img3 = Image.open('../data/canyon.png')
# # img3.show()
# img3_new = histo_equilization(img3)
# img3_new.show()

# img5 = Image.open('../data/church.png')
# # img5.show()
# img5_new = histo_equilization(img5)
# img5_new.show()

# img6 = Image.open('../data/chestXray.png')
# # img6.show()
# img6_new = histo_equilization(img6)
# img6_new.show()
