import numpy as np
import cv2
from cv2 import UMat
import matplotlib.pyplot as plt


image = cv2.imread('image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#### OpenCv histogram
# equ_image = cv2.equalizeHist(gray_image)

# # cv2.imshow(mat=gray_image, winname='normal')
# # cv2.imshow(mat=equ_image, winname='equ')

# plt.subplot(1, 2, 1)
# plt.hist(gray_image.ravel(), density=True, bins=30)
# plt.subplot(1, 2, 2)
# plt.hist(equ_image.ravel(), density=True, bins=30)
# plt.show()
# # cv2.waitKey()
#### Custom Histogram


max_pixel_value = gray_image.max(axis=(0,1))
L_max_value = np.log2(max_pixel_value)
if L_max_value is not int:
    L_max_value = int(L_max_value) + 1

pixeldict = dict()
for item in gray_image.ravel():
    if item in pixeldict:
        pixeldict[item] = pixeldict[item] + 1
    else:
        pixeldict[item] = 0

pixel_count = sum(pixeldict.values())

pixeldict ={k: v for k, v in sorted(pixeldict.items(), key=lambda item: item[0])}
pdf = {k: v / total for total in (pixel_count,) for k, v in pixeldict.items()}

cdf = pdf.copy()
summed_value = next(iter(pdf.values()))
for index, k in enumerate(pdf):
    if index == 0:
        summed_value = next(iter(pdf.values()))
    summed_value = cdf[k] + summed_value
    cdf[k] = summed_value

print(cdf)
