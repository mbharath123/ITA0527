import cv2

cap = cv2.VideoCapture("jyothiba.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

# 4:3 resolution
WIDTH = 640
HEIGHT = 480

delay = 30   # normal speed initially

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to 4:3 ratio
    frame_43 = cv2.resize(frame, (WIDTH, HEIGHT))

    cv2.imshow("Video (4:3 Ratio)", frame_43)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        delay = 150   # slow motion
        print("Slow motion")
    elif key == ord('n'):
        delay = 30    # normal speed
        print("Normal speed")
    elif key == ord('f'):
        delay = 5     # fast motion
        print("Fast motion")

cap.release()
cv2.destroyAllWindows()