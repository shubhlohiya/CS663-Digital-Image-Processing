import numpy as np
from PIL import Image

def der_x(image, x, y):
	try:
		cubic_plus = image[x+1][y]
		cubic_minus = image[x-1][y]

		der_X = (cubic_plus - cubic_minus) / 2.0

		return der_X
	#for last column
	except:
		cubic_minus = image[x-1][y]
		cubic = image[x][y]

		der_X = -1 * (cubic_minus - cubic)

		return der_X


def der_y(image, x, y):

	try:
		cubic_plus = image[x][y+1]
		cubic_minus = image[x][y-1]

		der_Y = (cubic_plus - cubic_minus) / 2.0

		return der_Y
	#for last row
	except :
		cubic_minus = image[x][y-1]
		cubic = image[x][y]

		der_Y = -1 * (cubic_minus - cubic)

		return der_Y

def der_xy(image, x, y):
	#for corner elements
	if x == image.shape[0]-1 and y == image.shape[1]-1:
		der_xy = (image[x][y] 
					- image[x-1][y] 
					- image[x][y-1] 
					+ image[x-1][y-1])
	elif x == image.shape[0]-1:
		der_xy = (image[x][y+1] 
					- image[x-1][y+1] 
					- image[x][y-1] 
					+ image[x-1][y-1]) / 2.0
	elif y == image.shape[1]-1:
		der_xy = (image[x+1][y] 
					- image[x-1][y] 
					- image[x+1][y-1] 
					+ image[x-1][y-1]) / 2.0
	else:
		der_xy = (image[x+1][y+1] 
					- image[x-1][y+1] 
					- image[x+1][y-1] 
					+ image[x-1][y-1]) / 4.0
	

	return der_xy 

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

	#(x1,y1)
	D = np.asarray([image[x1][y1], image[x2][y1], image[x1][y1], image[x2][y2],
			der_x(image, x1, y1), der_x(image, x2, y1), der_x(image, x1, y1), der_x(image, x2, y2),
			der_y(image, x1, y1), der_y(image, x2, y1), der_y(image, x1, y2), der_y(image, x2, y2),
			der_xy(image, x1, y1), der_xy(image, x2, y1), der_xy(image, x1, y2), der_xy(image, x2, y2)])


	return D.reshape((-1,1))

def calculate_para(image, x1, y1, x2, y2):

	#c.dot(para) = D
	
	C = coeff_matrix(x1, y1, x2, y2)
	D = der_matrix(image, x1, y1, x2, y2)

	para = np.linalg.inv(C).dot(D) 

	return para

def cubic_output(parameters, x, y):
	X = np.asarray([1, y, y**2, y**3,
			  x, x*y, x*(y**2), x*(y**3),
			  x**2, (x**2)*y, (x**2)*(y**2), (x**2)*(y**3),
			  x**3, (x**3)*y, (x**3)*(y**2), (x**3)*(y**3)])

	return X.dot(parameters)

def bicubic_for_a_rectangle(image, x1, y1, x2, y2):
	#assigning the interpolated value of to the pixel
	parameters = calculate_para(image, x1,y1, x2, y2)
	for i in range(x1, x2+1):
		for j in range(y1, y2+1):
			image[i][j] = cubic_output(parameters, i, j)
	return image

def bicubic(image):
	#converting both the images in numpt arrays
	image = np.asarray(image)
	#M is no. of rows and N is no. of columns in given image
	M = image.shape[0]
	N = image.shape[1]
	#initailizing the resultant image with zeros and given dimensions
	res_img = np.zeros((3*M-2, 2*N-1))

	#updating the pixel intensities accoding to given conditions
	#in rows, starting from element with index 0, every third element will be updated
	#in columns, startig from element with index 0, altenate elements will be updated

	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			res_img[i*3][j*2] = image[i][j]

	for i in range(image.shape[0] - 1):
		for j in range(image.shape[1] - 1):
			res_img = bicubic_for_a_rectangle(res_img, 3*i, 2*j, 3*i+3, 2*j+2)

	#converting array to the image
	res_img = Image.fromarray(res_img)
	return res_img


image = Image.open('../data/barbaraSmall.png')
img = bicubic(image)
img.show()