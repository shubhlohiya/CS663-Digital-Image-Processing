# Question 1 - Image Resizing and Rotation
import cv2
import numpy as np
from myBilinearInterpolation import myBilinearInterpolation
from myNearestNeighbour import myNearestNeighbour
from myBicubicInterpolation import myBicubicInterpolation
from myCompare import myCompare

from PIL import Image

# Question 1(a)

# Question 1(b)
image = cv2.imread("../data/barbaraSmall.png", 0)

# image = Image.open('../data/barbaraSmall.png')
large_bilinear = myBilinearInterpolation(image)

# Question 1(c)

large_nn = myNearestNeighbour(image)

# Question 1(d)

large_bicubic = myBicubicInterpolation(image)


myCompare(large_bilinear, large_nn , large_bicubic)

# Question 1(e)

# Question 1(f)
