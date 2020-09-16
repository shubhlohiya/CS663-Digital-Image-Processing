# Question 2 - Gray Transformation
import cv2
import numpy as np
import matplotlib.pyplot as plt
from myCLAHE import myCLAHE
import myForegroundMask
from myLinearContrastStretching import myLinearContrastStretching

# Question 2(a)
# image = cv2.imread("../data/statue.png", 0)
# mask = myForegroundMask.mask(image)

# masked_image = myForegroundMask.masking(image, mask)

# # Question 2(b)

# files = ["barbara", "TEM", "canyon", "retina", "church", "chestXray", "statue"]
# for i in files:
# 	rgb = 0 if i not in ["canyon", "church"] else 1
# 	image = cv2.imread(f"../data/{i}.png", rgb)
# 	if i=="statue":
# 		image = masked_image
# 	myLinearContrastStretching(image)
	
image = cv2.imread(f"../data/church.png", 1)
myLinearContrastStretching(image)


# Question 2(c)

# Question 2(d)

# Question 2(e)

# files = ["barbara", "canyon", "chestXray", "TEM"]

# for i in files:
# 	rgb = 0 if i != "canyon" else 1
# 	image = cv2.imread(f"../data/{i}.png", rgb)
# 	myCLAHE(image, i)



# image = cv2.imread(f"../data/{i}.png", rgb)
# myCLAHE(image, i)	
# plt.show()