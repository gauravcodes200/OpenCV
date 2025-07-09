import cv2
from datetime import datetime

# Open the default camera
cap = cv2.VideoCapture(0)

# Set high resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened. Press SPACE to capture image, or 'q' to quit.")

image_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Show the live preview
    cv2.imshow("Live Capture (Press SPACE to Capture, q to Quit)", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        print("Exiting.")
        break

    if key == 32:  # SPACE key
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"image_{timestamp}.jpg"
        cv2.imwrite(filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        image_count += 1
        print(f"[{image_count}] Image saved as {filename}")

cap.release()
cv2.destroyAllWindows()
print("Capture session complete.")