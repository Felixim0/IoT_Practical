import numpy as np
import cv2

camera = cv2.VideoCapture(0)
while camera.isOpened():
  ret, frame = camera.read()

  bimg = cv2.GaussianBlur(frame, (5, 5), 5)
  # please check what would happen if you don't smoothen the image first and consider why
  gray = cv2.cvtColor(bimg, cv2.COLOR_RGB2GRAY)
  circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=50,
  minRadius=50, maxRadius=200)
  circleMarkers = frame

  cv2.imshow('circles', circleMarkers)

  if circles is not None:
    circles = np.uint16(np.around(circles)) # numpy should be imported
    for i in circles[0, :]:
      cv2.circle(circleMarkers, (i[0], i[1]), i[2], color=[255, 0, 0], thickness=2) # draw circles
      cv2.circle(circleMarkers, (i[0], i[1]), 2, color=[0, 255, 0], thickness=2) # draw centroids
      #print(i[0], i[1]) # coordinates
      cv2.imshow('detected circles', circleMarkers)

  if cv2.waitKey(10) == 27:
    break

# esc to quit, or you can use cv2.waitKey(how many ms to wait) == ord('a') for "when a is pressed"
camera.release()
cv2.destroyAllWindows()

