
from __future__ import print_function
import cv2
from matplotlib import pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")




def showInMatplotlib(color_img, title, pos):
    """Shows an image using matplotlib capabilities"""
    # Convert BGR image to RGB
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(2, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')


def main():
    try:
        image = cv2.imread('Image_35.jpg', cv2.IMREAD_COLOR)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        fig = plt.figure(figsize=(15, 7))
        plt.suptitle("Adaptive thresholding", fontsize=14, fontweight='bold')
        fig.patch.set_facecolor('silver')

        # Perform adaptive thresholding with different parameters:
        thresh1 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        thresh2 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 3)
        thresh3 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        thresh4 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 3)

        # Plot the thresholded images:
        showInMatplotlib(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray img", 1)
        showInMatplotlib(cv2.cvtColor(thresh1, cv2.COLOR_GRAY2BGR), "method=THRESH_MEAN_C, blockSize=11, C=2",
                                 2)
        showInMatplotlib(cv2.cvtColor(thresh2, cv2.COLOR_GRAY2BGR), "method=THRESH_MEAN_C, blockSize=31, C=3",
                                 3)
        showInMatplotlib(cv2.cvtColor(thresh3, cv2.COLOR_GRAY2BGR), "method=GAUSSIAN_C, blockSize=11, C=2", 5)
        showInMatplotlib(cv2.cvtColor(thresh4, cv2.COLOR_GRAY2BGR), "method=GAUSSIAN_C, blockSize=31, C=3", 6)

        # Show the Figure:
        plt.show()

    except:
        pass


if __name__ == "__main__":
    main()









