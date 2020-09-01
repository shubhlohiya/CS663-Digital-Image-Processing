import numpy as np
import matplotlib.pyplot as plt


'''
Assuming the aspect ratio of the input image to be 1:1
The function myShrinkImageByFactorD takes the image and a factor
as input and return a shrinked image which is made by selecting every dth pixel in given image

the given function shows both the original and shrinked images so that we can clearly see Moire effects

'''

def myShrinkImageByFactorD(image, d): #image and shrinking factor d are inputs

	#initializing the resultant image by a numpy array of all zeros
	result_img = np.zeros((image.shape[0] // d, image.shape[1] // d))

	#travesing through the rows of image
	for i in range(image.shape[0]):
		#checking if the given row is multiple of d
		if (i + 1) % d == 0:
			#traversing through the columns of image
			for j in range(image.shape[1]):
				#checking if the given column is a multiple of d
				if (j + 1) % d == 0:
					#assigning the pixel intensity respective element of the result image
					result_img[(i+1)//d - 1][(j+1)//d - 1] = image[i][j]

	#converting the numpy array into a image
	plt.imshow(result_img, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title(f"Shrinked by a factor of {d}\n")
	plt.show() 

	#returning resultant image
	return result_img


