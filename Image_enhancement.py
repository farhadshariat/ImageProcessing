import numpy as np
import cv2
from cv2 import UMat
import matplotlib.pyplot as plt


image = cv2.imread('image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

equ_image = cv2.equalizeHist(gray_image)

# cv2.imshow(mat=gray_image, winname='normal')
# cv2.imshow(mat=equ_image, winname='equ')

plt.hist(gray_image.ravel(), density=True, bins=30)
plt.hist(equ_image.ravel(), density=True, bins=30)
plt.show()
plt.waitforbuttonpress()
# cv2.waitKey()