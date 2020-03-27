import sys
import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('src.bmp')
h = np.zeros((300,256,3))

bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]

for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)
    
    h=np.flipud(h)

    plt.imshow(h, cmap = 'hot', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  
    plt.show()