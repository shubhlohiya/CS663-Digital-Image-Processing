 # Question 1 - Image Resizing and Rotation
import cv2
import numpy as np
from PIL import Image
from myBiHistogramEqualiser import myBihistogram
from myBiHistogramEqualiser import histo_equilization

# Question 3(d)

# Bihistogram
img2 = Image.open('../data/pir.jpg')
myBihistogram(img2)

# Histogram
img1 = Image.open('../data/pir.jpg')
histo_equilization(img1)
