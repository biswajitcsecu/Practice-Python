


from __future__ import print_function
import cv2
import numpy as np


def main():
    try:
        im = cv2.imread("Image_36.jpg", cv2.IMREAD_GRAYSCALE)

        # Setup SimpleBlobDetector parameters.
        params = cv2.SimpleBlobDetector_Params()

        # Change thresholds
        params.minThreshold = 10
        params.maxThreshold = 200

        # Filter by Area.
        params.filterByArea = True
        params.minArea = 1500

        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0.1

        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0.87

        # Filter by Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.01

        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3:
            detector = cv2.SimpleBlobDetector(params)
        else:
            detector = cv2.SimpleBlobDetector_create(params)

        # Detect blobs.
        keypoints = detector.detect(im)

        # Draw detected blobs as red circles.

        im_with_keypoints = cv2.drawKeypoints(im,
                                keypoints, np.array([]), (0, 0, 255),
                                cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        # Show blobs
        cv2.imshow("Keypoints", im_with_keypoints)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except NotImplementedError:
        print("Error found")
        pass


if __name__ == "__main__":
    main()