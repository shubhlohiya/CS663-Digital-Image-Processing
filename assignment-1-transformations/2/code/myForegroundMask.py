import numpy as np
import matplotlib.pyplot as plt

'''
This function masks the image with the given reference
'''

def mask(image):  #given image is input
	
	#initializing resultant image with zeros
	mask = np.zeros(image.shape)
	#for grayscale images
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			if image[i][j] > 15:
				mask[i][j] = 255
	
	#converting numpy array to image
	plt.imshow(mask, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Binary mask\n")
	plt.show()

	return mask

def masking(image, mask):  #given image and reference mask image are inputs
		
	result_img = np.multiply(image, mask>0)

	#converting numpy array to image
	plt.imshow(result_img, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Masked Image\n")
	plt.show()

	return result_img