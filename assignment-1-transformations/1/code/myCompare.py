import numpy as np
import math
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def section(image):


	m=image.shape[0]
	n=image.shape[1]


	# x0 = (n-1)/2
	# y0 = (m-1)/2

	result_img=np.zeros((20,20))

	for i in range(20):
		for j in range(20):
			result_img[i][j]=image[i][j]


	# result_img = Image.fromarray(result_img)
	return result_img





def myCompare(bilinear , nn , bicubic): 


	# section_bilinear = np.zeros(bilinear.shape)

	plt.imshow(section(bilinear), cmap='jet', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Bilinear Interpolation - Barbara\n")
	plt.show()


	plt.imshow(section(nn), cmap='jet', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Nearest Neighbour - Barbara\n")
	plt.show()


	plt.imshow(section(bicubic), cmap='jet', vmin=0, vmax=255)
	plt.colorbar()
	plt.title("Bicubic - Barbara\n")
	plt.show()

	# for i in range(bilinear.shape[2]):
	# 	section_bilinear[:,:,i] = section(bilinear[:,:,i])
	# section_bilinear = Image.fromarray(result_img.astype('uint8'), 'RGB')
	# section_bilinear.show()

	# section_nn = np.zeros(nn.shape)
	# for i in range(nn.shape[2]):
	# 	section_nn[:,:,i] = section(nn[:,:,i])
	# section_nn = Image.fromarray(result_img.astype('uint8'), 'RGB')
	# section_nn.show()

	# section_bicubic = np.zeros(bicubic.shape)
	# for i in range(bicubic.shape[2]):
	# 	section_bicubic[:,:,i] = section(bicubic[:,:,i])
	# section_bicubic = Image.fromarray(result_img.astype('uint8'), 'RGB')
	# section_bicubic.show()