import numpy as np
from PIL import Image

'''
This function masks the image with the given reference
'''

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
	result_img = Image.fromarray(image, 'RGB')

	return result_img


PATH_IMAGE = '../data/retina.png'
image = Image.open(PATH_IMAGE)
image.show()
PATH_MASK = '../data/retinaMask.png'
mask = Image.open(PATH_MASK)

masked_image = masking(image, mask)
masked_image.show()
