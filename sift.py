# coding=utf-8
from __future__ import print_function
import warnings
import cv2

warnings.filterwarnings('ignore')


def main():
    try:
        img = cv2.imread('img18.png', cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        sift = cv2.ORB()
        kps, descriptors = sift.detectAndCompute(gray, None)

        cv2.drawKeypoints(img, kps, img, (51, 163, 236),
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv2.namedWindow('sift_keypoints', cv2.WINDOW_KEEPRATIO)
        cv2.imshow('sift_keypoints', img)
        cv2.waitKey()

    except NameError:
        print("Error found")
        pass


if __name__ == "__main__":
    print(__doc__)
    main()
    cv2.destroyAllWindows()
