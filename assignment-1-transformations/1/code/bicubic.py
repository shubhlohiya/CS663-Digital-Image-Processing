import numpy as np
from PIL import Image

def der_mat(image):
	der_mat = np.zeros((image.shape[0], image.shape[1], 3))

	num_row = image.shape[0]
	num_col = image.shape[1]

	for i in range(num_row):
		if i % 3 == 0:
			if i == 0:
				der_mat[i,:,0] = (image[i][:] - image[i+3][:])*(-1) / 3
			elif i == num_row - 1:
				der_mat[i,:,0] = (image[i][:] - image[i-3][:]) / 3
			else:
				der_mat[i,:,0] = (image[i+3][:] - image[i-3][:]) / 6

	for i in range(num_col):
		if i % 2 == 0:
			if i == 0:
				der_mat[i,:,1] = (((image[:][i] - image[:][i+2])*(-1)) / 2).T
			elif i == num_col - 1:
				der_mat[i,:,1] = ((image[:][i] - image[:][i-2]) / 2).T
			else:
				der_mat[i,:,1] = ((image[:][i+2] - image[:][i-2]) / 4).T

	for i in range(num_row):
		if i % 3 == 0 or i == 0:
			for j in range(num_col):
				if j % 2 == 0 or j == 0:
					if j == 0:
						if i == 0:
							der_mat[i,j,2] = (image[i+3][j+2] - image[i][j+2] - image[i+3][j] + image[i][j]) / 6
						elif i == num_row - 1:
							der_mat[i,j,2] = (image[i][j+2] - image[i-3][j+2] - image[i][j] + image[i-3][j]) / 6
						else:
							der_mat[i,j,2] = (image[i+3][j+2] - image[i-3][j+2] - image[i+3][j] + image[i-3][j]) / 12

					if j == num_col - 1:
						if i == 0:
							der_mat[i,j,2] = (image[i+3][j] - image[i][j] - image[i+3][j-2] + image[i][j-2]) / 6
						elif i == num_row - 1:
							der_mat[i,j,2] = (image[i][j] - image[i-3][j] - image[i][j-2] + image[i-3][j-2]) / 6
						else:
							der_mat[i,j,2] = (image[i+3][j] - image[i-3][j] - image[i+3][j-2] + image[i-3][j-2]) / 12
					
					if i == 0 and j != 0 and j != num_col - 1:
						der_mat[i,j,2] = (image[i+3][j+2] - image[i][j+2] - image[i+3][j-2] + image[i][j-2]) / 12
					if i == num_row - 1 and j != 0 and j != num_col - 1:
						der_mat[i,j,2] = (image[i][j+2] - image[i-3][j+2] - image[i][j-2] + image[i-3][j-2]) / 12

					elif num_row - 1 > i > 0 and num_col - 1 > j > 0:
						der_mat[i,j,2] = (image[i+3][j+2] - image[i-3][j+2] - image[i+3][j-2] + image[i-3][j-2]) / 24

	return der_mat


def coeff_matrix(x1, y1, x2, y2):


	C = np.zeros((16,16))

	'''
	this function creates a matrix form coefficients of a00, a01, ... in those 16 constraints given
	'''

	#(x1, y1)
	C[0] = [1, y1, y1**2, y1**3,
			  x1, x1*y1, x1*(y1**2), x1*(y1**3),
			  x1**2, (x1**2)*y1, (x1**2)*(y1**2), (x1**2)*(y1**3),
			  x1**3, (x1**3)*y1, (x1**3)*(y1**2), (x1**3)*(y1**3)] 

	#(x2, y1)
	C[1] = [1, y1, y1**2, y1**3,
			  x2, x2*y1, x2*(y1**2), x2*(y1**3),
			  x2**2,(x2**2)*y1, (x2**2)*(y1**2), (x2**2)*(y1**3),
			  x2**3, (x2**3)*y1, (x2**3)*(y1**2), (x2**3)*(y1**3)]

	#(x1, y2)
	C[2] = [1, y2, y2**2, y2**3,
			  x1, x1*y2, x1*(y2**2), x1*(y2**3),
			  x1**2, (x1**2)*y2, (x1**2)*(y2**2), (x1**2)*(y2**3),
			  x1**3, (x1**3)*y2, (x1**3)*(y2**2), (x1**3)*(y2**3)]

	#(x2, y2)
	C[3] = [1, y2, y2**2, y2**3,
			  x2, x2*y2, x2*(y2**2), x2*(y2**3), 
			  x2**2, (x2**2)*y2, (x2**2)*(y2**2), (x2**2)*(y2**3),
			  x2**3, (x2**3)*y2, (x2**3)*(y2**2), (x2**3)*(y2**3)]

	#der_w.r.t_x
	#(x1, y1)
	C[4] = [0, 0, 0, 0,
			  1, 1*y1, 1*(y1**2), 1*(y1**3),
			  x1*2, (x1*2)*y1, (x1*2)*(y1**2), (x1*2)*(y1**3),
			  3*x1**2, 3*(x1**2)*y1, 3*(x1**2)*(y1**2), 3*(x1**2)*(y1**3)] 
	
	#(x2, y1)
	C[5] = [0, 0, 0, 0,
			  1, 1*y1, 1*(y1**2), 1*(y1**3),
			  x2*2, (x2*2)*y1, (x2*2)*(y1**2), (x2*2)*(y1**3),
			  3*x2**2, 3*(x2**2)*y1, 3*(x2**2)*(y1**2), 3*(x2**2)*(y1**3)]

	#(x1, y2)
	C[6] = [0, 0, 0, 0,
			  1, 1*y2, 1*(y2**2), 1*(y2**3),
			  x1*2, (x1*2)*y2, (x1*2)*(y2**2), (x1*2)*(y2**3),
			  3*x1**2, 3*(x1**2)*y2, 3*(x1**2)*(y2**2), 3*(x1**2)*(y2**3)]

	#(x2, y2)
	C[7] = [0, 0, 0, 0,
			  1, 1*y2, 1*(y2**2), 1*(y2**3),
			  x2*2, (x2*2)*y2, (x2*2)*(y2**2), (x2*2)*(y2**3),
			  3*x2**2, 3*(x2**2)*y2, 3*(x2**2)*(y2**2), 3*(x2**2)*(y2**3)]

	#der_w.r.t_y
	#(x1, y1)
	C[8] = [0, 1, y1*2, 3*y1**2,
			  0, x1*1, x1*(y1*2), x1*(3*y1**2),
			  0, (x1**2)*1, (x1**2)*(y1*2), (x1**2)*(3*y1**2),
			  0, (x1**3)*1, (x1**3)*(y1*2), (x1**3)*(3*y1**2)]

	#(x2, y1)
	C[9] = [0, 1, y1*2, 3*y1**2,
			  0, x2*1, x2*(y1*2), x2*(3*y1**2),
			  0, (x2**2)*1, (x2**2)*(y1*2), (x2**2)*(3*y1**2),
			  0, (x2**3)*1, (x2**3)*(y1*2), (x2**3)*(3*y1**2)]

	#(x1, y2)
	C[10] = [0, 1, y2*2, 3*y2**2,
			  0, x1*1, x1*(y2*2), x1*(3*y2**2),
			  0, (x1**2)*1, (x1**2)*(y2*2), (x1**2)*(3*y2**2),
			  0, (x1**3)*1, (x1**3)*(y2*2), (x1**3)*(3*y2**2)]

	#(x2, y2)
	C[11] = [0, 1, y2*2, 3*y2**2,
			  0, x2*1, x2*(y2*2), x2*(3*y2**2),
			  0, (x2**2)*1, (x2**2)*(y2*2), (x2**2)*(3*y2**2),
			  0, (x2**3)*1, (x2**3)*(y2*2), (x2**3)*(3*y2**2)]


	#der_w.r.t_xy
	#(x1, y1)
	C[12] = [0, 0, 0, 0,
			  0, 1, 1*(y1*2), 1*(3*y1**2),
			  0, (x1*2)*1, (x1*2)*(y1*2), (x1*2)*(3*y1**2),
			  0, (3*x1**2)*1, (3*x1**2)*(y1*2), (3*x1**2)*(3*y1**2)]

	#(x2, y1)
	C[13] = [0, 0, 0, 0,
			  0, 1, 1*(y1*2), 1*(3*y1**2),
			  0, (x2*2)*1, (x2*2)*(y1*2), (x2*2)*(3*y1**2),
			  0, (3*x2**2)*1, (3*x2**2)*(y1*2), (3*x2**2)*(3*y1**2)]

	#(x1, y2)
	C[14] = [0, 0, 0, 0,
			  0, 1, 1*(y2*2), 1*(3*y2**2),
			  0, (x1*2)*1, (x1*2)*(y2*2), (x1*2)*(3*y2**2),
			  0, (3*x1**2)*1, (3*x1**2)*(y2*2), (3*x1**2)*(3*y2**2)]
			  		  
	#(x2, y2)
	C[15] = [0, 0, 0, 0,
			  0, 1, 1*(y2*2), 1*(3*y2**2),
			  0, (x2*2)*1, (x2*2)*(y2*2), (x2*2)*(3*y2**2),
			  0, (3*x2**2)*1, (3*x2**2)*(y2*2), (3*x2**2)*(3*y2**2)]

	
	return C


def der_matrix(image, x1, y1, x2, y2):
	D = np.zeros((16,1))
	mat = der_mat(image)

	#(x1,y1)
	D = np.asarray([image[x1][y1], image[x2][y1], image[x1][y1], image[x2][y2],
			mat[x1, y1, 0], mat[x2, y1, 0], mat[x1, y2, 0], mat[x2, y2, 0],
			mat[x1, y1, 1], mat[x2, y1, 1], mat[x1, y2, 1], mat[x2, y2, 1],
			mat[x1, y1, 2], mat[x2, y1, 2], mat[x1, y2, 2], mat[x2, y2, 2]])


	return D.reshape((-1,1))




def bilin_interpol_image(image):
	#converting both the images in numpt arrays
	image = np.asarray(image)
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

	print(der_mat(res_img))

image = Image.open('../data/barbaraSmall.png')
image = np.asarray(image)
print(der_matrix(image, 0, 0, 3, 2))