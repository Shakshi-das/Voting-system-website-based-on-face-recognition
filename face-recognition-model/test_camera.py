import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("❌ Cannot open camera")
else:
    print("✅ Camera opened successfully")
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Test", frame)
        cv2.waitKey(0)
    cam.release()
    cv2.destroyAllWindows()
