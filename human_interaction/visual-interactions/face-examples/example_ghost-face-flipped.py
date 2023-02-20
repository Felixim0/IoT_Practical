import cv2
import numpy as np
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally to correct the orientation of the numbers.
    image_flipped = cv2.flip(image, 1)

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image_flipped.flags.writeable = False
    image_flipped = cv2.cvtColor(image_flipped, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_flipped)

    # Draw the face mesh annotations on the image.
    image_flipped.flags.writeable = True
    image_flipped = cv2.cvtColor(image_flipped, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        # Draw the landmark numbers.
        for idx, landmark in enumerate(face_landmarks.landmark):
            x, y = int((1 - landmark.x) * image.shape[1]), int(landmark.y * image.shape[0])
            cv2.putText(image_flipped, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)

    # Flip the image horizontally again to return it to its original orientation.
    image = cv2.flip(image_flipped, 1)

    cv2.imshow('MediaPipe Face Mesh', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()

