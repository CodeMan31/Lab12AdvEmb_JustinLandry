import cv2 as cv
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')  # used to detect the argument
# in this case it the front of a face described by an xml file
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')   # used to detect the argument
# in this case it is the eyes described by an xml file
cap = cv.VideoCapture(0)  # creates a video variable


while cv.waitKey(1) == -1:  # while nop key is pressed
    success, frame = cap.read()     # creates a image variable, also determines if video was captured properly
    if success:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, minSize=(40, 40))

            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(frame, (x+ex, y+ey),(x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        cv.imshow('Face Detection', frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

# This program uses xml files to interrogate a video and detect, if a face is
# include in the video.  #
