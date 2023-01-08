import cv2

# Capture video from the roadway
cap = cv2.VideoCapture("roadway.mp4")

# Set up the reference frame
_, reference_frame = cap.read()
reference_frame = cv2.cvtColor(reference_frame, cv2.COLOR_BGR2GRAY)

# Set up the foreground mask
fg_mask = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)

# Set up the blob detector
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 100
params.maxArea = 10000
detector = cv2.SimpleBlobDetector_create(params)

# Set up the tracker
tracker = cv2.MultiTracker_create()

# Process each frame
while True:
    # Read the frame and convert it to grayscale
    _, frame = cap.read()
    if frame is None:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compute the foreground mask
    fg_mask.apply(frame, learningRate=-1)
    mask = fg_mask.getBackgroundImage()

    # Detect blobs in the mask
    keypoints = detector.detect(mask)

    # Update the tracker with the new keypoints
    tracker.add(cv2.TrackerMedianFlow_create(), mask, keypoints)

    # Update the tracker and get the updated positions
    _, boxes = tracker.update(mask)

    # Draw the bounding boxes and keypoints
    for box in boxes:
        x, y, w, h = [int(i) for i in box]
        cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.drawKeypoints(mask, keypoints, mask, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display the frame
    cv2.imshow("Car Motion Detector", mask)
    if cv2.waitKey(1) == 27:
        break

# Release the video capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
