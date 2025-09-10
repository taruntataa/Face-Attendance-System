import pickle
import cv2
import pandas as pd
from datetime import datetime
from deepface import DeepFace

# Load stored face embeddings
with open("face_embeddings.pkl", "rb") as f:
    face_db = pickle.load(f)

# Initialize camera
video = cv2.VideoCapture(0)

attendance_log = "attendance.csv"

while True:
    ret, frame = video.read()
    faces = DeepFace.find(img_path=frame, db_path="dataset", model_name="Facenet")

    if len(faces) > 0:
        recognized_person = faces[0]['identity'].split('/')[-2]
        print(f"Recognized: {recognized_person}")

        # Log attendance
        df = pd.read_csv(attendance_log)
        if recognized_person not in df["Name"].values:
            df.loc[len(df)] = [recognized_person, datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
            df.to_csv(attendance_log, index=False)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == 27:  # Press 'Esc' to stop
        break

video.release()
cv2.destroyAllWindows()
