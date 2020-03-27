
from __future__ import print_function, division
import cv2
import numpy as np


def main():
    img = cv2.imread('41.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    # To detect only sharp corners
    dst = cv2.cornerHarris(gray, blockSize=4, ksize=5, k=0.04)
    # Result is dilated for marking the corners
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image
    img[dst > 0.01 * dst.max()] = [0, 0, 0]
    cv2.namedWindow('Harris Corners Sharp', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('Harris Corners Sharp', img)

    # to detect soft corners
    dst = cv2.cornerHarris(gray, blockSize=14, ksize=5, k=0.04)
    dst = cv2.dilate(dst, None)
    img[dst > 0.01 * dst.max()] = [0, 0, 0]

    cv2.namedWindow('Harris Corners', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('Harris Corners', img)
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
