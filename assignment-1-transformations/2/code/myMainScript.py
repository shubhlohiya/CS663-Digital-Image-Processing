# Question 2 - Gray Transformation
import cv2
import numpy as np
import matplotlib.pyplot as plt
from myCLAHE import myCLAHE

# Question 2(a)

# Question 2(b)

# Question 2(c)

# Question 2(d)

# Question 2(e)

files = ["barbara", "canyon", "chestXray", "TEM"]

for i in files:
	rgb = 0 if i != "canyon" else 1
	image = cv2.imread(f"../data/{i}.png", rgb)
	myCLAHE(image, i)
	
plt.show()