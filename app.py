from fastapi import FastAPI, UploadFile, File
import os
import cv2
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Load recognizer and Haar cascade (update paths if needed)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")  # Make sure model is trained
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

@app.get("/create-dataset/")
def create_dataset():
    cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    face_id = 1  # You can later get this from the frontend
    count = 0

    if not os.path.exists('dataset'):
        os.makedirs('dataset')

    while True:
        ret, img = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"dataset/User.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])

        if count >= 30:
            break

    cam.release()
    return {"message": f"30 face samples collected for user ID {face_id}"}



@app.get("/train/")
def train_model():
    os.system("python train-model.py")
    return {"message": "Model training complete."}


@app.post("/recognize-face/")
async def recognize_face(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("L")
    img_np = np.array(image)

    faces = face_cascade.detectMultiScale(img_np, 1.3, 5)
    if len(faces) == 0:
        return {"error": "No face detected."}

    x, y, w, h = faces[0]
    roi = img_np[y:y + h, x:x + w]

    label, confidence = recognizer.predict(roi)
    return {"label": int(label), "confidence": float(confidence)}


@app.get("/test-camera/")
def test_camera():
    # Not ideal for API – better to run from script directly
    os.system("python test_camera.py")
    return {"message": "Camera test started. (Check local window)"}


