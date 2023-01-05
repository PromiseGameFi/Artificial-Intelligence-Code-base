import cv2

# Capture video from a video file or a webcam
cap = cv2.VideoCapture("video.mp4")

# Set the frame width and height
cap.set(3, 640)
cap.set(4, 480)

# Read the first frame
_, prev_frame = cap.read()

# Convert the frame to grayscale and blur it
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (5, 5), 0)

while True:
    # Read the next frame
    _, frame = cap.read()

    # Check if the video has reached the end
    if frame is None:
        break

    # Convert the frame to grayscale and blur it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the difference between the current and previous frames
    diff = cv2.absdiff(prev_gray, gray)

    # Threshold the difference image
    _, thresh = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the contours
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Set the current frame as the previous frame for the next iteration
    prev_gray = gray

    # Check for user input
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the video capture device
cap.release()

# Close all windows
cv2.destroyAllWindows()
