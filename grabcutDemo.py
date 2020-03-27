# coding=utf-8

from  __future__ import print_function
import numpy as np
import cv2
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')


def main():
    original = cv2.imread('img6.png')
    img = original.copy()
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    rect = (100, 1, 420, 378)
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]

    #Display
    fig = plt.figure(figsize=(9,7))
    ax = fig.gca()
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("grabcut")
    plt.xticks([])
    plt.yticks([])
    #Segment
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.title("original")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.close(fig)



if __name__ == '__main__':
    main()