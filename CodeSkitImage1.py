# coding=utf-8

from __future__ import print_function
import numpy as np
import scipy as sp
from skimage import io
from skimage import *
from scipy import ndimage as ndi
import matplotlib.pyplot  as plt
from skimage import data, color
import toolz as tz
from toolz import curried as c
from glob import glob
import itertools as it
import vtk


def gaussian_kernel(size, sigma):
    positions = np.arange(size) - size // 2
    kernel_raw = np.exp(-positions**2 / (2 * sigma**2))
    kernel_normalized = kernel_raw / np.sum(kernel_raw)
    return kernel_normalized


def main():
    img = io.imread('34.jpg',as_gray=False)
    img_gray = color.rgb2gray(img)
    nrows, ncols = img.shape[:2]
    print("Type:", type(img), "Shape:", img.shape, "Data type:", img.dtype)

    smooth_diff = np.zeros(img.shape[:2], np.float64)
    diff2d = np.array([[0, 1, 0], [1, 0, -1], [0, -1, 0]])
    #smooth_diff = ndi.convolve(gaussian_kernel(3, 3), np.float64(img))
    #_edges = ndi.convolve(np.float64(img) , diff2d)

    shifted = ndi.shift(img_gray, (0, 50))

    print(vtk.VTK_BUILD_VERSION)
    #image show
    plt.imshow(img)
    #plt.figure()

    fig, axes = plt.subplots(nrows=1, ncols=2)
    axes[0].imshow(img_gray)
    axes[0].set_title('Original')
    axes[1].imshow(shifted)
    axes[1].set_title('Shifted');
    plt.show()
    plt.close(fig)





if __name__ == "__main__":
    main()
