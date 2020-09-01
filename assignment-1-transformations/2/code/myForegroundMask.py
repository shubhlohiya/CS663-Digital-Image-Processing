import numpy as np
from PIL import Image

'''
This function masks the image with the given reference
'''

def mask(image):  #given image is input
	#converting the image to numpy array
	image = np.asarray(image)
	#initializing resultant image with zeros
	mask = np.zeros(image.shape)
	#for grayscale images
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			if image[i][j] > 15:
				mask[i][j] = 255
	
	#converting numpy array to image
	mask = Image.fromarray(mask)

	return mask

def masking(image, mask):  #given image and reference mask image are inputs
	#converting both the images in numpt arrays
	image = np.asarray(image)
	mask = np.asarray(mask)

	#initializing resultant image with zeros
	result_img = np.zeros(image.shape)
	#for grayscale images
	if len(image.shape) == 2:
		result_img = np.multiply(image, mask)
	else:
		#masking each of the three RGB channels
		for i in range(image.shape[2]):
			result_img[:,:,i] = np.multiply(image[:,:,i], mask)

	#converting numpy array to image
	result_img = Image.fromarray(image)

	return result_img

image= Image.open('../data/statue.png')
mask = mask(image)
mask.show('../data/mask.png')
res_image = masking(image, mask)
res_image.show()
res_image.save('../data/masked_satue.png')

