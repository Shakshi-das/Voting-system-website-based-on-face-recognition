import cv2
import os

# Initialize webcam
cam = cv2.VideoCapture(0)  # Try 1 or 2 if this doesn't work

# Initialize face detector
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# ✅ SAFETY CHECKS
if face_detector.empty():
    print("[ERROR] Haar cascade not loaded. Make sure 'haarcascade_frontalface_default.xml' is in the same folder.")
    exit()

if not cam.isOpened():
    print("[ERROR] Cannot access camera. Try changing the index (0, 1, 2...) or check if another app is using it.")
    exit()

# Begin capturing
face_id = input('Enter user ID: ')
print("[INFO] Capturing face. Look at the camera...")

count = 0
while True:
    ret, img = cam.read()
    if not ret:
        print("[ERROR] Failed to grab frame from camera.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        count += 1
        cv2.imwrite(f"dataset/user.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('image', img)
    if cv2.waitKey(100) & 0xFF == ord('q') or count >= 30:
        break

cam.release()
cv2.destroyAllWindows()
