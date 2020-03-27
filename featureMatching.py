

import sys
import argparse
import cv2
import numpy as np


def argument_parser():
    parser = argparse.ArgumentParser(description='Stitch two images together')
    parser.add_argument("--query-image", dest="query_image", required=True,
                        help="First image that needs to be stitched")
    parser.add_argument("--train-image", dest="train_image", required=True,
                        help="Second image that needs to be stitched")
    parser.add_argument("--min-match-count", dest="min_match_count", type=int,
                        required=False, default=10, help="Minimum number of matches required")
    return parser


# Warp img2 to img1 using the homography matrix H
def warpImages(img1, img2, H):
    rows1, cols1 = img1.shape[:2]
    rows2, cols2 = img2.shape[:2]

    list_of_points_1 = np.float32([[0, 0], [0, rows1], [cols1, rows1], [cols1, 0]]).reshape(-1, 1, 2)
    temp_points = np.float32([[0, 0], [0, rows2], [cols2, rows2], [cols2, 0]]).reshape(-1, 1, 2)
    list_of_points_2 = cv2.perspectiveTransform(temp_points, H)
    list_of_points = np.concatenate((list_of_points_1, list_of_points_2), axis=0)

    [x_min, y_min] = np.int32(list_of_points.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(list_of_points.max(axis=0).ravel() + 0.5)
    translation_dist = [-x_min, -y_min]
    H_translation = np.array([[1, 0, translation_dist[0]], [0, 1, translation_dist[1]], [0, 0, 1]])

    output_img = cv2.warpPerspective(img2, H_translation.dot(H), (x_max - x_min, y_max - y_min))
    output_img[translation_dist[1]:rows1 + translation_dist[1], translation_dist[0]:cols1 + translation_dist[0]] = img1

    return output_img



def main(min_match_count=None):
    img1 = cv2.imread('pic13.jpg', 0)  # queryImage
    img2 = cv2.imread('pic14.jpg', 0)  # trainImage
    # args = argument_parser().parse_args()
    # img1 = cv2.imread(args.query_image, 0)
    # img2 = cv2.imread(args.train_image, 0)
    # min_match_count = args.min_match_count

    # cv2.imshow('Query image', img1)
    # cv2.imshow('Train image', img2)
    cv2.imshow('Frame 1', img1)
    cv2.imshow('Frame 2', img2)

    # Initialize the SIFT detector
    sift = cv2.ORB_create()

    # Extract the keypoints and descriptors
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # Initialize parameters for Flann based matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=15)
    search_params = dict(checks=150)

    # Compute the matches
    bf =cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    # Draw first 10 matches.
    img3 = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches[:10], None, flags=2)

    cv2.imshow("Match", img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
