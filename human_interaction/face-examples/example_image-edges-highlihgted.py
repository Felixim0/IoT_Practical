import cv2
camera = cv2.VideoCapture(0)

while camera.isOpened():
  ret, frame = camera.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  cv2.imshow('Gray image', gray)
  ret, blackwhite = cv2.threshold(gray, 40, 110, cv2.THRESH_BINARY_INV)
  cv2.imshow('Binary image', blackwhite)

  edges = cv2.Canny(gray, 50, 150)
  cv2.imshow('Edges', edges)
  corners = cv2.cornerHarris(gray, 3, 5, 0.06)
  # corners = cv2.dilate(corners, None)
  cornerMarkers = frame
  cornerMarkers[corners > 0.01 * corners.max()] = [0, 0, 255]
  cv2.imshow('Corners', cornerMarkers)
    
  if cv2.waitKey(10) == 27:
    break


# esc to quit, or you can use cv2.waitKey(how many ms to wait) == ord('a') for "when a is pressed"
camera.release()
cv2.destroyAllWindows()
