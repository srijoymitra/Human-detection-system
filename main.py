import cv2

# === Load pre-recorded video ===
video = cv2.VideoCapture(r'C:\Users\profa\OneDrive\Pictures\Camera Roll\samplevdo.mp4')

# Create a background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Resize for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Find contours of the moving areas
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:  # Filter out small movements/noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show result
    cv2.imshow('Human Movement Detection', frame)
    cv2.imshow('Foreground Mask', fgmask)

    # Exit on pressing 'q'
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

# Cleanup
video.release()
cv2.destroyAllWindows()