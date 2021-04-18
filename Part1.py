import cv2 as cv
import sys

img = cv.imread('babyyoda.jpg')  # cv.imread: function that returns an image variable based arg file name

res = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)

if img is None:  # can't find image
    sys.exit("The image could not be read.")  # exits with the argument as text
# cv.imshow("OpenCV Image", img)  # cv.imshow: function that shows argument image, and title argument string
cv.imshow("OpenCV Image", res)  # shows baby yoda!
cv.waitKey(0)  # waits for key "0" to be pressed
cv.destroyAllWindows()  # clean up
