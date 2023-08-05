import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# VideoCapture(0) 0= hame kon sa web cam use kar rahe hai.
video_capture = cv2.VideoCapture(0)

# load known faces
mohit_img = face_recognition.load_image_file("faces/mohit.png")
# face encoding image ko number mein convert kar rahe hai so that it is easier to compare.
mohit_encoding = face_recognition.face_encodings(mohit_img)[0]

# nitin_img = face_recognition.load_image_file("faces/nitin.png")
# nitin_encoding = face_recognition.face_encodings(nitin_img)[0]

# known_face_encodings = [mohit_encoding, nitin_encoding]
# known_face_name = ["Mohit", "Nitin"]

known_face_encodings = [mohit_encoding]
known_face_name = ["Mohit"]

# list of expected student
students = known_face_name.copy()

# image mein face ki location
face_locations = []
face_encoding = []

# get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv","w+",newline="")
lnwriter = csv.writer(f)

while True:
    # _ video capture is successful or not, frame
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize face
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        # argmin tell distance and jab distance minimum hoga tab sab se jyda similar hoga
        best_match_index = np.argmin(face_distance)

        # matches ke andar true false value hai jo bata rahe hai ki face match bhi hua hai ki nahi.
        if( matches [ best_match_index ]):
            name = known_face_name[best_match_index]

        # Add a text if a person is present
        if name in known_face_name:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10,100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame , name+"Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

    cv2.imshow("Attendance",frame)
    # jab bhi mai q press karu toh while break ho jaye
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

# we are realeaing the video
video_capture.release()
cv2.destroyAllWindows()
f.close()
