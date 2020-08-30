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



def cdf(image):

	#frequency of occurance of each intensity initialized to zero
	freq = np.zeros((256,)) 
	#going through each element of array to count the number of occurance if each intensity
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			freq_val = image[i][j]
			freq[freq_val] += 1

	#nitializing the cdf by zeros
	cdf = np.zeros((256,))
	#probability of selecting one pixel form original image
	prob = 1.0 / (image.shape[0] * image.shape[1])
	#updating the cdf
	for i in range(256):
		for j in range(i+1):
			cdf[i] += freq[j] * prob


	return cdf

def histo_match_grayscale(image1, image2):
	cdf1 = cdf(image1)
	cdf2 = cdf(image2)

	#matrix for inv_cdf2(cdf1) initailized with zeros
	new_pix_int = np.zeros((256,))
	#finding the inverse
	for i in range(256):
		new_pix_int[i] = np.argmin(abs(cdf1[i] - cdf2))
	#iniatializing the resultant image with zeros
	res_img = np.zeros(image1.shape)
	#updating the pixel intensities with new ones after histogram matching
	for i in range(image1.shape[0]):
		for j in range(image1.shape[1]):
			int_val = image1[i][j]
			res_img[i][j] = new_pix_int[int_val]

	return res_img

def histo_match_rgb(image1, image2):
		#converting both the images in numpt arrays
	image1 = np.asarray(image1)
	image2 = np.asarray(image2)

	#for grayscale
	if len(image1.shape) == 2:
		return Image.fromarray(histo_match_grayscale(image1, image2))
		#for color image
	else:
		res_img = np.zeros(image1.shape)
		for i in range(image1.shape[2]):
			res_img[:,:,i] = histo_match_grayscale(image1[:,:,i], image2[:,:,i])

		res_img = Image.fromarray(res_img.astype('uint8'))
		return res_img


img1 = Image.open('../data/retina.png')
img1.show('original image')
img2 = Image.open('../data/retinaRef.png')

img = histo_match_rgb(img1, img2)
img.show('histogram_match_image')

img3 = histo_equilization(img1)
img3.show('histogram_equilization_image')
