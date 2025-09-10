import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
name = input("Enter your Name: ")
os.makedirs(f"dataset/{name}", exist_ok=True)

count = 0
while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        face = frame[y:y+h, x:x+w]
        cv2.imwrite(f"dataset/{name}/{count}.jpg", face)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Capture", frame)
    if cv2.waitKey(1) == 27 or count >= 50:  # Press 'Esc' to stop
        break

video.release()
cv2.destroyAllWindows()
