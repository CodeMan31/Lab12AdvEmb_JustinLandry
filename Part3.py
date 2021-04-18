import numpy as np
import cv2 as cv
import sys

img1 = cv.imread('bbyoda.jpg')  # sets file to image variable
img2 = cv.imread('bbyoda1.jpg')  # sets file to image variable
alpha = 0.5  # variable used to determine how much the images are blended
dst = cv.addWeighted(img1, 1 - alpha, img2, alpha, 0)  # blends two images based on arguments and returns blended image
cv.imshow('dst', dst)  # shows image dst with title dst
cv.waitKey(0)   # waits for key '0'
cv.destroyAllWindows()  # clean up

#   This program could be used to create a graphics editor like
#   like photoshop pr to detect motion in an image. #
