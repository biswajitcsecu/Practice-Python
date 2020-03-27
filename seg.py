

import sys
import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np

  
image = cv2.imread('src.bmp') 

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pixel_values = image.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)
  

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

# number of clusters (K)
k = 3
_, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)

segmented_image = centers[labels.flatten()]

segmented_image = segmented_image.reshape(image.shape)


plt.imshow(segmented_image, interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  
plt.show()


















