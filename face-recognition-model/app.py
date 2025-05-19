from fastapi import FastAPI, UploadFile, File
import os
import io
import subprocess
import cv2
import numpy as np
from PIL import Image

app = FastAPI()

# ====== Constants and Paths ======
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAINER_PATH = os.path.join( "trainer", "trainer.yml")
CASCADE_PATH = os.path.join( "face recognition model", "haarcascade_frontalface_default.xml")
DATASET_DIR = os.path.join( "dataset")

# ====== Load Recognizer and Haar Cascade once at startup ======
if not os.path.exists(TRAINER_PATH):
    raise FileNotFoundError("❌ Trainer file not found. Train the model first.")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(TRAINER_PATH)

face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
if face_cascade.empty():
    raise FileNotFoundError("❌ Haar cascade file not found.")

# ====== Utility: Enhance lighting (CLAHE) ======
def apply_clahe(gray_img):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray_img)

# ====== Routes ======

@app.post("/create-dataset/")
def create_dataset(face_id: int = 1):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        return {"error": "❌ Cannot open camera. Please check your camera connection."}

    os.makedirs(DATASET_DIR, exist_ok=True)
    count = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = apply_clahe(gray)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            count += 1
            file_path = os.path.join(DATASET_DIR, f"User.{face_id}.{count}.jpg")
            cv2.imwrite(file_path, gray[y:y+h, x:x+w])

        if count >= 30:
            break

    cam.release()
    return {"message": f"✅ 30 face samples collected for user ID {face_id}"}


@app.get("/train/")
def train_model():
    try:
        result = subprocess.run(["python", "train-model.py"], capture_output=True, text=True)
        return {"message": "✅ Model training complete.", "output": result.stdout}
    except Exception as e:
        return {"error": f"❌ {str(e)}"}


@app.post("/recognize-face/")
async def recognize_face(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("L")
        img_np = np.array(image)

        img_np = apply_clahe(img_np)

        faces = face_cascade.detectMultiScale(
            img_np,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if len(faces) == 0:
            return {"error": "❌ No face detected."}

        x, y, w, h = faces[0]
        roi = img_np[y:y+h, x:x+w]

        label, confidence = recognizer.predict(roi)

        identity = f"User {label}" if confidence < 60 else "Unknown"

        return {
            "identity": identity,
            "label": int(label),
            "confidence": float(confidence),
            "confidence_readable": f"{100 - confidence:.2f}% match"
        }

    except Exception as e:
        return {"error": f"❌ Error during face recognition: {str(e)}"}


@app.get("/test-camera/")
def test_camera():
    try:
        result = subprocess.run(["python", "test_camera.py"], capture_output=True, text=True)
        return {"message": "✅ Camera test script executed.", "output": result.stdout}
    except Exception as e:
        return {"error": f"❌ {str(e)}"}

