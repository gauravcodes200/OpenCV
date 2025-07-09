import cv2
from datetime import datetime
import time

# Configuration
duration_seconds = 10                    # Recording duration in seconds
frame_width = 1280
frame_height = 720
fps = 20.0

# Generate filename with datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"recording_{timestamp}.mp4"

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define codec and video writer for MP4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For .mp4 format
out = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

print(f"Recording started. Saving to '{filename}' for {duration_seconds} seconds...")

# Start timer
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    # Add timestamp to frame
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cv2.putText(frame, current_time, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    # Write frame to file and show preview
    out.write(frame)
    cv2.imshow('Recording', frame)

    # Stop after fixed duration
    if time.time() - start_time > duration_seconds:
        break

    # Optional: allow early stop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Recording finished. File saved as '{filename}'")