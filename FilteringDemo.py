
from matplotlib import pyplot as plt
import cv2
import numpy as np
import torch
import kornia
import torchvision



def main():
    try:
        img_bgr: np.ndarray = cv2.imread('model8.png', cv2.IMREAD_COLOR)
        x_bgr: torch.Tensor = kornia.image_to_tensor(img_bgr)
        x_rgb: torch.Tensor = kornia.bgr_to_rgb(x_bgr)
        x_rgb = x_rgb.expand(2, -1, -1, -1)
        x_rgb = x_rgb.float() / 255.

        imshow(x_rgb)
        # Box Blur
        x_blur: torch.Tensor = kornia.box_blur(x_rgb, (9, 9))
        imshow(x_blur)
        # Median Blur
        x_blur: torch.Tensor = kornia.median_blur(x_rgb, (5, 5))
        imshow(x_blur)
        # Gaussian Blur
        x_blur: torch.Tensor = kornia.gaussian_blur2d(x_rgb, (11, 11), (11., 11.))
        imshow(x_blur)

    except:
        print("Error found")


def imshow(input: torch.Tensor):
        fig = plt.figure(figsize=(8,6), dpi=150)
        out: torch.Tensor = torchvision.utils.make_grid(input, nrow=2, padding=1)
        out_np: np.ndarray = kornia.tensor_to_image(out)
        plt.imshow(out_np)
        plt.axis('off')
        plt.show()
        plt.close(fig)




if __name__ == "__main__":
    main()