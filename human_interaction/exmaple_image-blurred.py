import cv2
camera = cv2.VideoCapture(0)

while camera.isOpened():
  ret, frame = camera.read()
  img2 = cv2.blur(frame, (10, 10))
  cv2.imshow('Averaging blurred', img2)
  img3 = cv2.GaussianBlur(frame, (3, 3), 1.5)
  cv2.imshow('Gaussian blurred', img3)
  img4 = cv2.bilateralFilter(frame, 5, 20, 50)
  cv2.imshow('Bilateral blurred', img4)
  if cv2.waitKey(10) == 27:
    break


# esc to quit, or you can use cv2.waitKey(how many ms to wait) == ord('a') for "when a is pressed"
camera.release()
cv2.destroyAllWindows()
