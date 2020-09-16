import numpy as np
import math
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def bilin_interpol_intensity(image , x, y): #function takes four corners of a rectangle and an image with a point in which we are going to do the interpolation 
  
    x1 = math.floor(x)
    x2 = x1 + 1
    y1 = math.floor(y)
    y2 = y1 + 1


    if x1 < 0 or x2<0 or x1>= image.shape[1] or x2 >= image.shape[1] or y1 < 0 or y2 < 0 or y1 >= image.shape[0] or y2 >= image.shape[0]:
    	return 0

    # if(y2>image.shape[1]):
    # 	return image[y1-1][x1]
    # else:
    # 	if (x2>image.shape[0]):
    # 		return image[y1][x1-1]

    
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



def rotate_image(image,angle):

	M = image.shape[0]
	N = image.shape[1]
	#M is no. of rows and N is no. of columns in given image
	

	res_img = np.zeros((M,N))

	# for j in range(N):
	# 	res_img[0][j]=image[0][j]
	# 	res_img[M-1][j]=image[M-1][j]

	# for i in range(M):
	# 	res_img[i][0]=image[i][0]
	# 	res_img[i][N-1]=image[i][M-1]


	# finding the center
	x0 = (N-1)//2
	y0 = (M-1)//2

	for i in range(N):
		for j in range(M):

			x = i - x0
			y = y0 - j

			r = np.sqrt(pow(x,2) + pow (y,2))

			if x == 0 :

				if y == 0:
					res_img[i][j] = image[x0][y0]
					continue

				else:

					if y<0 :
						theta = 1.5 * math.pi
					else :
						theta = 0.5 * math.pi

			else:

				if y==0:
					if x<0:
						theta= math.pi
					else:
						theta= 0

				else:
					if x>0 and y>0:
						theta = np.arctan(y/x)

					if x<0 and y>0:
						theta = 0.5*math.pi + np.arctan(x/(-1*y))

					if x>0 and y<0:
						theta = 1.5*math.pi + np.arctan(x/(-1*y))

					if x<0 and y<0:
						theta = math.pi + np.arctan(y/x)
	        

			xr = r*np.cos(theta + ((math.pi/180)*angle))
			yr = r*np.sin(theta + ((math.pi/180)*angle))

			xtrue = xr + x0
			ytrue = y0 - yr

			res_img[i][j]= bilin_interpol_intensity(image,xtrue,ytrue)


	# a = np.sqrt(pow(x-1,2) + pow (y-1,2))
	# theta = np.arctan( (x-1) / (y-1) )



	# x0 = x - a*np.sin(theta - angle)
	# y0 = y - a*np.cos(theta - angle)

	# print(x0)
	# print(y0)

	# xi = x0
	# yi = y0
	# for j in range(1,M-1):
	# 	for i in range(1,N-1):
	# 		res_img[i][j]= bilin_interpol_intensity(image,xi,yi)
	# 		xi = xi + np.sin(theta - angle)
	# 		yi = yi + np.cos(theta - angle)

	# 	xi = xi - ((N-2)* np.sin(theta - angle)) - np.cos(theta - angle)
	# 	yi = yi - ((N-2)* np.cos(theta - angle)) + np.sin(theta - angle)




	# print(res_img)
	plt.imshow(image, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Original Image\n")
	plt.show()

	plt.imshow(res_img, cmap='gray', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Image Rotation 30 degrees\n")
	plt.show()



