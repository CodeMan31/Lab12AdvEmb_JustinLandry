import cv2 as cv
import numpy as np

img = cv.imread('lines.jpg')    # reads image from lines.jpg file
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # makes image gray
edges = cv.Canny(gray, 50, 120)  # detects edges with in the gray image
# variable declarations:
minLineLength = 20
maxLineGap = 5
lines = cv.HoughLinesP(edges, 1, np.pi / 180.0, 20, minLineLength, maxLineGap)  # used to detect straight lines

for x1, y1, x2, y2 in lines[6]:
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv.imshow("edges", edges)
    cv.imshow("lines", img)

cv.waitKey()
cv.destroyAllWindows()

# this program could also be used to create image manipulation software,
# image analysis software or could also be used to used to count specific
# shapes in an image; you could uses that data to recognize a specific object#
