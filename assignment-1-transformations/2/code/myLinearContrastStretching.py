import numpy as np
import matplotlib.pyplot as plt
import cv2


'''

this function does piecewise linear contrast streching for the given image
it considers three linear pieces for mapping intensities
the pieces are:
1st  -  (0,0) -> (x1, y1)
2nd  -  (x1, y1) -> (x2, y2)
3rd  -  (x2, y2) -> (255, 255)

'''

def line_output(x1, y1, x2, y2, x):
	# (x1, y1), (x2, y2) are given points on the line
	# x is between x1 and x2 and the function calculated the value after linear interpolation of between given two points

	slope = (y1-y2)/(x1-x2)

	y = x * slope - x1 * slope + y1

	return y

def linear_contrast_update(intensity, x1, y1, x2, y2):

	#mapping the intensities according to the three pieces of line

	if intensity <= x1:
		return line_output(0,0,x1,y1,intensity)
	elif intensity >= x2:
		return line_output(x2, y2, 255, 255, intensity)
	else:
		return line_output(x1, y1, x2, y2, intensity)

#vectorizing the function so that it will be able to operate on numpy arrays
linear_contrast_update_np = np.vectorize(linear_contrast_update)



def myLinearContrastStretching(img):

	#iniatilizing result image with zeros and original image shape
	img_res = np.zeros(img.shape)

	#for grayscale image updating the inntensities
	if len(img.shape) == 2:
		img_res = linear_contrast_update_np(img, x1, y1, x2, y2)
		plt.imshow(img_res, cmap='gray', vmin=0, vmax=255)
		plt.colorbar()
		plt.title("LinearContrastStretching\n")
		plt.show()
		return

	#updating intensities for each channel in color images	
	else:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		for i in range(img.shape[2]):
			img_res[:,:,i] = linear_contrast_update_np(img[:,:,i], x1, y1, x2, y2)
		
		plt.imshow(img_res)
		plt.colorbar()
		plt.title("LinearContrastStretching\n")
		plt.show()
		return

x1, y1 = 70, 10
x2, y2 = 190, 250



#using 7th image with mask
# img7 = Image.open('/home/prathmesh/Desktop/IITB/CS663/CS663-Digital-Image-Processing/assignment-1-transformations/2/data/statue.png')
# img7.show()
# mask = Image.open('/home/prathmesh/Desktop/IITB/CS663/CS663-Digital-Image-Processing/assignment-1-transformations/2/data/retinaMask.png')
# masked_image = masking(img7, mask)
# transform(masked_image)

