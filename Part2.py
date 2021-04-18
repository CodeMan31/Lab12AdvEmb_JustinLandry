import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)
    # cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
        cv.imwrite('exitimage.jpg', gray)
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

# This program could be very useful in variety of applications. Being able
# to capture images means you can do things with that image like face recognition,
# you could use to it work as vision for a robot, you could use it for motion
# control, etc. In conclusion this could be a very fundamental part of a variety of
# very cool advanced applications. #
