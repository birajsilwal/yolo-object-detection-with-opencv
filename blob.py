# importing the required libraries
import cv2
import numpy as np

# loading the image containing blobs
# img = cv2.imread('images/blob_original_image/blob_o_1.jpg', 0)
# img = cv2.imread('images/blob_original_image/original_image.png', 0)
# img = cv2.imread('images/blob_original_image/centroid.jpg', 0)
img = cv2.imread('images/living_room.jpg', 0)

# creating an object named 'detector' for SimpleBlobDetector() class
# for openCV versions 3.x & above this class is replaced by SimpleBlobDetector_create() class
detector = cv2.SimpleBlobDetector_create()
# detect blobs by passing input image into the detector
# keypoints refers to the spatial locations or points in the image that have something in common, for e.g. threshold value
# keypoints are special because they are scale-invariant i.e. whether the image rotates,translates,shrinks/expands or distorts,
# the key points remains same even in the modified image
keypoints = detector.detect(img)

# # draw blobs on our image as red circles
# blank = np.zeros((1, 1))
# blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
#
# # to display total number of blobs detected
# number_of_blobs = len(keypoints)
# text = "Total: " + str(len(keypoints))
# cv2.putText(blobs, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#
# # displaying image with blob keypoints
# cv2.imshow('blobs using default parameters', blobs)
# cv2.waitKey(0)

# filtering out specific size such as circle

# # to differentiate the circular blobs from non-circular blobs, we need to set some parameters
# # these parameters can be set by using the functions of SimpleBlobDetector_Params() class
#
# setting filtering parameters
# firstly, creating an object to access SimpleBlobDetector_params() class functions
params = cv2.SimpleBlobDetector_Params()

# set area filtering parameters
# in this, we can define both min as well as max area for the blob
params.filterByArea = False
params.minArea = 0
#
# set circularity filtering parameters
# the minCircularity value =1 defines a perfect circle & 0 defines it's opposite
params.filterByCircularity = False
params.minCircularity = 0

# # set convexity filtering parameters
params.filterByConvexity = False
params.minConvexity = 0
#
# setting inertia filtering parameters
params.filterByInertia = False
params.minInertiaRatio = 0

# creating a detector with the specified parameters
detector = cv2.SimpleBlobDetector_create(params)
# detect circular blobs
keypoints = detector.detect(img)

# draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

# displaying number of circular blobs detected
number_of_blobs = len(keypoints)
text = "Total: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# highlighting circular blobs among several blobs
cv2.imshow('blobs', blobs)
cv2.waitKey(0)

cv2.destroyAllWindows()
