import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

if not vid.isOpened:
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = vid.read()
    # if frame is read correctly ret is True

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow("canny2", cv.Canny(frame, 180, 140))  # shows the canny image 180 and 140 seem to detect me the best

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
vid.release()

# This program could be used if you needed to simplify an image in order to analyze
# If you wanted to write a program to determine the shape of something it would make it
# more simple to just view the lines.#


