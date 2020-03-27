

from __future__ import print_function
import sys
import cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def main():

    try:
        img = cv2.imread('model10.png')
        rows, cols = img.shape[:2]

        # generating vignette mask using Gaussian kernels
        kernel_x = cv2.getGaussianKernel(cols, 200)
        kernel_y = cv2.getGaussianKernel(rows, 200)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        output = np.copy(img)

        # applying the mask to each channel
        for i in range(3):
            output[:, :, i] = output[:, :, i] * mask

        #display output
        cv2.imshow('Original', img)
        cv2.imshow('Vignette', output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except FileNotFoundError:
        print("Error found")
        sys.exit(0)



if __name__ == '__main__':
        main()

