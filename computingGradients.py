# coding=utf-8


import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
  image = cv2.imread('img9.png', cv2.IMREAD_GRAYSCALE)
  dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
  dy = cv2.Sobel(image, cv2.CV_32F, 0, 1)



  cv2.namedWindow("src", cv2.WINDOW_AUTOSIZE)
  cv2.namedWindow("horizontal", cv2.WINDOW_AUTOSIZE)
  cv2.namedWindow("vertical", cv2.WINDOW_AUTOSIZE)
  cv2.imshow("src", image)
  cv2.imshow("horizontal", dx)
  cv2.imshow("vertical", dy)

  cv2.waitKey(0)
  cv2.destroyAllWindows()


  plt.figure(figsize=(8,3))
  plt.subplot(131)
  plt.axis('off')
  plt.title('image')
  plt.imshow(image, cmap='gray')
  plt.subplot(132)
  plt.axis('off')
  plt.imshow(dx, cmap='gray')
  plt.title(r'$\frac{dI}{dx}$')
  plt.subplot(133)
  plt.axis('off')
  plt.title(r'$\frac{dI}{dy}$')
  plt.imshow(dy, cmap='gray')
  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  main()
