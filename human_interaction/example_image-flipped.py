import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
  ret, frame = camera.read()
  cv2.imshow('original', frame)
  img1 = cv2.flip(frame, -1)
  cv2.imshow('flipped', img1)
  if cv2.waitKey(10) == 27:
    break

# esc to quit, or you can use cv2.waitKey(how many ms to wait) == ord('a') for "when a is pressed"
camera.release()
cv2.destroyAllWindows()
