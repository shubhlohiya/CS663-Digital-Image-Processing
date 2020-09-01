import numpy as np
import matplotlib.pyplot as plt

def bilin_interpol_intensity(image ,x1, y1, x2, y2, x, y): #function takes four corners of a rectangle and an image with a point in which we are going to do the interpolation 
                                          #this function returns intersity after interpolation at (x,y)
    #pixel intensity at the corners
    Q11 = image[x1][y1]
    Q12 = image[x1][y2]
    Q22 = image[x2][y2]
    Q21 = image[x2][y1]

    #computing the interpolated value
    Q_inter = (Q11 * ((x2 - x) / (x2 - x1)) * ((y2 - y) / (y2 - y1))
    		+ Q21 * ((x - x1) / (x2 - x1)) * ((y2 - y) / (y2 - y1))
    		+ Q12 * ((x2 - x) / (x2 - x1)) * ((y - y1) / (y2 - y1))
    		+ Q22 * ((x - x1) / (x2 - x1)) * ((y - y1) / (y2 - y1)))
    return Q_inter

 
def bilin_interpol(image, x1, y1, x2, y2):

	#assigning the interpolated value of to the pixel
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			image[i][j] = bilin_interpol_intensity(image, x1, y1, x2, y2, i, j)
	return image

def myBilinearInterpolation(image):
	
	#M is no. of rows and N is no. of columns in given image
	M = image.shape[0]
	N = image.shape[1]

	#initailizing the resultant image with zeros and given dimensions
	res_img = np.zeros((3*M-2, 2*N-1))
	#print(res_img.shape)

	#updating the pixel intensities accoding to given conditions
	#in rows, starting from element with index 0, every third element will be updated
	#in columns, startig from element with index 0, altenate elements will be updated

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			res_img[i*3][j*2] = image[i][j]

	#using bi-linear interpolation between each rectangel formed
	for i in range(image.shape[0] - 1):
		for j in range(image.shape[1] - 1):
			res_img = bilin_interpol(res_img, 3*i, 2*j, 3*i+3, 2*j+2)

	#converting array to the image
	plt.imshow(res_img, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Bilinear Interpolation - Barbara\n")
	plt.show()

	return res_img