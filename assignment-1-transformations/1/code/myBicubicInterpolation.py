import numpy as np
import matplotlib.pyplot as plt

def der_mat(image):
	der_mat = np.zeros((image.shape[0], image.shape[1], 3))

	num_row = image.shape[0]
	num_col = image.shape[1]
	#x derivatives
	for i in range(num_row):
		if i % 3 == 0:
			#for 1st row
			if i == 0:
				der_mat[i,:,0] = (image[i][:] - image[i+3][:])*(-1)
			#for last row
			elif i == num_row - 1:
				der_mat[i,:,0] = (image[i][:] - image[i-3][:])
			#for rows inbetween
			else:
				der_mat[i,:,0] = (image[i+3][:] - image[i-3][:])

	for i in range(num_col):
		if i % 2 == 0:
			#for 1st column
			if i == 0:
				der_mat[i,:,1] = (((image[:][i] - image[:][i+2])*(-1))).T
			#for last column
			elif i == num_col - 1:
				der_mat[i,:,1] = ((image[:][i] - image[:][i-2])).T
			#for columns inbetween
			else:
				der_mat[i,:,1] = ((image[:][i+2] - image[:][i-2])).T

	for i in range(num_row):
		if i % 3 == 0 or i == 0:
			for j in range(num_col):
				if j % 2 == 0 or j == 0:
					#for 1st column
					if j == 0:
						if i == 0:
							der_mat[i,j,2] = (image[i+3][j+2] - image[i][j+2] - image[i+3][j] + image[i][j])
						elif i == num_row - 1:
							der_mat[i,j,2] = (image[i][j+2] - image[i-3][j+2] - image[i][j] + image[i-3][j])
						else:
							der_mat[i,j,2] = (image[i+3][j+2] - image[i-3][j+2] - image[i+3][j] + image[i-3][j])

					#for last column
					if j == num_col - 1:
						if i == 0:
							der_mat[i,j,2] = (image[i+3][j] - image[i][j] - image[i+3][j-2] + image[i][j-2])
						elif i == num_row - 1:
							der_mat[i,j,2] = (image[i][j] - image[i-3][j] - image[i][j-2] + image[i-3][j-2])
						else:
							der_mat[i,j,2] = (image[i+3][j] - image[i-3][j] - image[i+3][j-2] + image[i-3][j-2])
					#for 1st row
					if i == 0 and j != 0 and j != num_col - 1:
						der_mat[i,j,2] = (image[i+3][j+2] - image[i][j+2] - image[i+3][j-2] + image[i][j-2])
					#for last row
					if i == num_row - 1 and j != 0 and j != num_col - 1:
						der_mat[i,j,2] = (image[i][j+2] - image[i-3][j+2] - image[i][j-2] + image[i-3][j-2])
					#everywhere else
					elif num_row - 1 > i > 0 and num_col - 1 > j > 0:
						der_mat[i,j,2] = (image[i+3][j+2] - image[i-3][j+2] - image[i+3][j-2] + image[i-3][j-2])

	return der_mat


def coeff_matrix(x1, y1, x2, y2):


	C = np.zeros((16,16))

	'''
	this function creates a matrix form coefficients of a00, a01, ... in those 16 constraints given
	'''

	#(x1, y1)
	C[0] = np.asarray([1, y1, y1**2, y1**3,
			  x1, x1*y1, x1*(y1**2), x1*(y1**3),
			  x1**2, (x1**2)*y1, (x1**2)*(y1**2), (x1**2)*(y1**3),
			  x1**3, (x1**3)*y1, (x1**3)*(y1**2), (x1**3)*(y1**3)]) 

	#(x2, y1)
	C[1] = np.asarray([1, y1, y1**2, y1**3,
			  x2, x2*y1, x2*(y1**2), x2*(y1**3),
			  x2**2,(x2**2)*y1, (x2**2)*(y1**2), (x2**2)*(y1**3),
			  x2**3, (x2**3)*y1, (x2**3)*(y1**2), (x2**3)*(y1**3)])

	#(x1, y2)
	C[2] = np.asarray([1, y2, y2**2, y2**3,
			  x1, x1*y2, x1*(y2**2), x1*(y2**3),
			  x1**2, (x1**2)*y2, (x1**2)*(y2**2), (x1**2)*(y2**3),
			  x1**3, (x1**3)*y2, (x1**3)*(y2**2), (x1**3)*(y2**3)])

	#(x2, y2)
	C[3] = np.asarray([1, y2, y2**2, y2**3,
			  x2, x2*y2, x2*(y2**2), x2*(y2**3), 
			  x2**2, (x2**2)*y2, (x2**2)*(y2**2), (x2**2)*(y2**3),
			  x2**3, (x2**3)*y2, (x2**3)*(y2**2), (x2**3)*(y2**3)])

	#der_w.r.t_x
	#(x1, y1)
	C[4] = np.asarray([0, 0, 0, 0,
				  1, 1*y1, 1*(y1**2), 1*(y1**3),
				  x1*2, (x1*2)*y1, (x1*2)*(y1**2), (x1*2)*(y1**3),
				  3*x1**2, 3*(x1**2)*y1, 3*(x1**2)*(y1**2), 3*(x1**2)*(y1**3)]) 
	
	#(x2, y1)
	C[5] = np.asarray([0, 0, 0, 0,
				  1, 1*y1, 1*(y1**2), 1*(y1**3),
				  x2*2, (x2*2)*y1, (x2*2)*(y1**2), (x2*2)*(y1**3),
				  3*x2**2, 3*(x2**2)*y1, 3*(x2**2)*(y1**2), 3*(x2**2)*(y1**3)])

	#(x1, y2)
	C[6] = np.asarray([0, 0, 0, 0,
				  1, 1*y2, 1*(y2**2), 1*(y2**3),
				  x1*2, (x1*2)*y2, (x1*2)*(y2**2), (x1*2)*(y2**3),
				  3*x1**2, 3*(x1**2)*y2, 3*(x1**2)*(y2**2), 3*(x1**2)*(y2**3)])

	#(x2, y2)
	C[7] = np.asarray([0, 0, 0, 0,
				  1, 1*y2, 1*(y2**2), 1*(y2**3),
				  x2*2, (x2*2)*y2, (x2*2)*(y2**2), (x2*2)*(y2**3),
				  3*x2**2, 3*(x2**2)*y2, 3*(x2**2)*(y2**2), 3*(x2**2)*(y2**3)])

	#der_w.r.t_y
	#(x1, y1)
	C[8] = np.asarray([0, 1, y1*2, 3*y1**2,
				  0, x1*1, x1*(y1*2), x1*(3*y1**2),
				  0, (x1**2)*1, (x1**2)*(y1*2), (x1**2)*(3*y1**2),
				  0, (x1**3)*1, (x1**3)*(y1*2), (x1**3)*(3*y1**2)])

	#(x2, y1)
	C[9] = np.asarray([0, 1, y1*2, 3*y1**2,
				  0, x2*1, x2*(y1*2), x2*(3*y1**2),
				  0, (x2**2)*1, (x2**2)*(y1*2), (x2**2)*(3*y1**2),
				  0, (x2**3)*1, (x2**3)*(y1*2), (x2**3)*(3*y1**2)])

	#(x1, y2)
	C[10] = np.asarray([0, 1, y2*2, 3*y2**2,
				  0, x1*1, x1*(y2*2), x1*(3*y2**2),
				  0, (x1**2)*1, (x1**2)*(y2*2), (x1**2)*(3*y2**2),
				  0, (x1**3)*1, (x1**3)*(y2*2), (x1**3)*(3*y2**2)])

	#(x2, y2)
	C[11] = np.asarray([0, 1, y2*2, 3*y2**2,
				  0, x2*1, x2*(y2*2), x2*(3*y2**2),
				  0, (x2**2)*1, (x2**2)*(y2*2), (x2**2)*(3*y2**2),
				  0, (x2**3)*1, (x2**3)*(y2*2), (x2**3)*(3*y2**2)])

	#der_w.r.t_xy
	#(x1, y1)
	C[12] = np.asarray([0, 0, 0, 0,
				  0, 1, 1*(y1*2), 1*(3*y1**2),
				  0, (x1*2)*1, (x1*2)*(y1*2), (x1*2)*(3*y1**2),
				  0, (3*x1**2)*1, (3*x1**2)*(y1*2), (3*x1**2)*(3*y1**2)])

	#(x2, y1)
	C[13] = np.asarray([0, 0, 0, 0,
				  0, 1, 1*(y1*2), 1*(3*y1**2),
				  0, (x2*2)*1, (x2*2)*(y1*2), (x2*2)*(3*y1**2),
				  0, (3*x2**2)*1, (3*x2**2)*(y1*2), (3*x2**2)*(3*y1**2)])

	#(x1, y2)
	C[14] = np.asarray([0, 0, 0, 0,
				  0, 1, 1*(y2*2), 1*(3*y2**2),
				  0, (x1*2)*1, (x1*2)*(y2*2), (x1*2)*(3*y2**2),
				  0, (3*x1**2)*1, (3*x1**2)*(y2*2), (3*x1**2)*(3*y2**2)])
			  		  
	#(x2, y2)
	C[15] = np.asarray([0, 0, 0, 0,
				  0, 1, 1*(y2*2), 1*(3*y2**2),
				  0, (x2*2)*1, (x2*2)*(y2*2), (x2*2)*(3*y2**2),
				  0, (3*x2**2)*1, (3*x2**2)*(y2*2), (3*x2**2)*(3*y2**2)])

	
	return C


def der_matrix(mat,image, x1, y1, x2, y2):
	D = np.zeros((16,1))
	

	#(x1,y1)
	D = np.asarray([image[x1][y1], image[x2][y1], image[x1][y1], image[x2][y2],
			mat[x1, y1, 0], mat[x2, y1, 0], mat[x1, y2, 0], mat[x2, y2, 0],
			mat[x1, y1, 1], mat[x2, y1, 1], mat[x1, y2, 1], mat[x2, y2, 1],
			mat[x1, y1, 2], mat[x2, y1, 2], mat[x1, y2, 2], mat[x2, y2, 2]])


	return D.reshape((-1,1))

def calculate_para(mat, image, x1, y1, x2, y2):


	
	C = coeff_matrix(x1, y1, x2, y2)
	D = der_matrix(mat, image, x1, y1, x2, y2)

	para = np.linalg.inv(C).dot(D) 

	return para

def cubic_output(parameters, x, y):
	X = np.asarray([1, y, y**2, y**3,
			  x, x*y, x*(y**2), x*(y**3),
			  x**2, (x**2)*y, (x**2)*(y**2), (x**2)*(y**3),
			  x**3, (x**3)*y, (x**3)*(y**2), (x**3)*(y**3)])

	return X.dot(parameters)

def bicubic_for_a_rectangle(mat, image, x1, y1, x2, y2):
	#assigning the interpolated value of to the pixel
	parameters = calculate_para(mat, image, x1,y1, x2, y2)
	for i in range(x1, x2):
		for j in range(y1, y2):
			image[i][j] = cubic_output(parameters, i, j)
	return image

def myBicubicInterpolation(image):
	
	#M is no. of rows and N is no. of columns in given image
	M = image.shape[0]
	N = image.shape[1]
	#initailizing the resultant image with zeros and given dimensions
	res_img = np.zeros((3*M-2, 2*N-1))
	mat = der_mat(res_img)
	#updating the pixel intensities accoding to given conditions
	#in rows, starting from element with index 0, every third element will be updated
	#in columns, startig from element with index 0, altenate elements will be updated

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			res_img[i*3][j*2] = image[i][j]

	for i in range(image.shape[0] - 1):

		for j in range(image.shape[1] - 1):
			res_img = bicubic_for_a_rectangle(mat,res_img, 3*i, 2*j, 3*i+3, 2*j+2)

	#converting array to the image
	plt.imshow(res_img, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Bicubic Interpolation - Barbara\n")
	plt.show()
	
	return res_img