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
		Histo_equi_single_channel(image).show()
	else:
		
		#for color image, doing the equilization for each channel
		result_img = np.zeros(image.shape)
		for i in range(image.shape[2]):
			result_img[:,:,i] = Histo_equi_single_channel(image[:,:,i])
		result_img = Image.fromarray(result_img.astype('uint8'), 'RGB')
		result_img.show()



def bihisto_equilization(image):
	# To find 'a'= median intensity

	#frequency of occurance of each intensity initialized to zero
	freq = np.zeros((256, 1)) 
	#going through each element of array to count the number of occurance if each intensity
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			inten_val = image[i][j]
			freq[inten_val] += 1



	#frequency of occurance of a pixel inrensity in resultant image initialized to zero
	b = np.zeros((256, 1))
	#probability of picking a particular pixel from input image
	prob_one_pix = 1.0 / (image.shape[0] * image.shape[1])


	

	#equating CDF of a to b and finding 'i' s.t. CDF is just >= 0.5. this i will be median intensity. let median = median intensity
	median=(-1)
	for i in range(256):
		for j in range(i+1):
			b[i] += freq[j] * prob_one_pix
			
		if median==(-1) and b[i]>=0.5:
			median=i
	
	# total no of pixels in the domain [0,median] , then no of pixels in (median,255] = (image.shape[0] * image.shape[1]) - total
	total=0

	for i in range(median+1):
		total = total + freq[i]


	#equating CDF in domain [0,median] and scaling it with median as CDF is between (0,1) which maps it to [0,median]
	for i in range(median + 1):
		for j in range(i+1):
			b[i] += freq[j] / total
		b[i] = nearest_int( b[i]*median)
		
	#equating CDF in domain (median, 255] and scaling it with (255-median) as CDF is between (0,1) to map it to (median,255)
	for i in range(median + 1 , 256):
		for j in range(i,i+1):
			b[i] += freq[j] / ((image.shape[0] * image.shape[1])-total)
		#rounding off to nearest integer
		b[i] = nearest_int(median + b[i] * (255-median))
		

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




def biHistogram(image):
	#converting both the images in numpt arrays
	image = np.asarray(image)
	# for grayscale image
	if len(image.shape) == 2:
		bihisto_equilization(image).show()
	else:
		#for color image, doing the equilization for each channel
		result_img = np.zeros(image.shape)
		for i in range(image.shape[2]):
			result_img[:,:,i] = bihisto_equilization(image[:,:,i])
		result_img = Image.fromarray(result_img.astype('uint8'), 'RGB')
		result_img.show()








