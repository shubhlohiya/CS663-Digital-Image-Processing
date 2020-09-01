# Question 1 - Image Resizing and Rotation
import cv2
import numpy as np
from myShrinkImageByFactorD import myShrinkImageByFactorD
from myBilinearInterpolation import myBilinearInterpolation
from myNearestNeighbour import myNearestNeighbour
from myBicubicInterpolation import myBicubicInterpolation

# Question 1(a)
image = cv2.imread("../data/circles_concentric.png", 0)

# shrinking by a factor of 2
myShrinkImageByFactorD(image, 2)

# shrinking by a factor of 3
myShrinkImageByFactorD(image, 3)


# Question 1(b)
image = cv2.imread("../data/barbaraSmall.png", 0)
large_bilinear = myBilinearInterpolation(image)

# Question 1(c)

large_nn = myNearestNeighbour(image)

# Question 1(d)

large_bicubic = myBicubicInterpolation(image)



# Question 1(e)


# Question 1(f)
