from deepface import DeepFace
import os
import cv2
import numpy as np

face_db = {}  # Dictionary to store embeddings

for person in os.listdir("dataset"):
    person_path = os.path.join("dataset", person)
    for image in os.listdir(person_path):
        img_path = os.path.join(person_path, image)
        embedding = DeepFace.represent(img_path, model_name="Facenet")
        face_db[person] = embedding[0]['embedding']

# Save embeddings for future recognition
import pickle
with open("face_embeddings.pkl", "wb") as f:
    pickle.dump(face_db, f)
