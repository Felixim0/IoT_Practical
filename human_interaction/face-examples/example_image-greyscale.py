import cv2
camera = cv2.VideoCapture(0)

while camera.isOpened():
  ret, frame = camera.read()

  gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
  cv2.imshow('Gray image', gray)
  ret, blackwhite = cv2.threshold(gray, 40, 110, cv2.THRESH_BINARY_INV)
  cv2.imshow('Binary image', blackwhite)
  
  if cv2.waitKey(10) == 27:
    break


# esc to quit, or you can use cv2.waitKey(how many ms to wait) == ord('a') for "when a is pressed"
camera.release()
cv2.destroyAllWindows()
