import sys
import cv2
import dlib
import time
import csv

#Define frame size
frame_height = 540
frame_width = 960
"""
frame_height = 720
frame_width = 1280
"""
flag = 1
# Create CSV file
with open('dane.csv', 'w') as new_file:
    writer = csv.writer(new_file)

# Initialize filter
### face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\shape_predictor_68_face_landmarks.dat")

# Capture video from deafult webcam
captured_video = cv2.VideoCapture(0)
captured_video.set(3, frame_width)
captured_video.set(4, frame_height)

# Editing coordinates 
def norm_coord(rect_x1, rect_y1, rect_x2, rect_y2 ,coord_x, coord_y):
    width = rect_x2 - rect_x1
    height = rect_y2 - rect_y1
    mid_x = rect_x2 - width/2
    mid_y = rect_y2 - height/2
    new_coord_x = (coord_x-mid_x)/width*2
    new_coord_y = (coord_y-mid_y)/-height*2
    new_coord_x = round(new_coord_x, 3)
    new_coord_y = round(new_coord_y, 3)
    return(new_coord_x, new_coord_y)

while(captured_video.isOpened()):
    # Obtain a frame from video and flip it
    ret, frame = captured_video.read()
    frame = cv2.flip(frame, 1)
    # Draw a circle at middle
    cv2.circle(frame, (int(frame_width/2), int(frame_height/2)), 2, (0, 0, 255), 1)
    # Convert frame to grey
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Face detection
    faces = detector(gray_frame)
    # Get the highest point of face
    for face in faces:
        landmarks = predictor(gray_frame, face)
        if landmarks.part(19).y < landmarks.part(24).y:
            rect_point = landmarks.part(19).y
        else:
            rect_point = landmarks.part(24).y

        # Draw rectangle around detected face
        cv2.rectangle(frame, (landmarks.part(0).x, rect_point), (landmarks.part(16).x, landmarks.part(8).y), (0, 0, 255), 1)
        # Draw a black circle at the middle of the face rectangle
        cv2.circle(frame, (int(landmarks.part(0).x+((landmarks.part(16).x-landmarks.part(0).x)/2)), (int(landmarks.part(8).y-(landmarks.part(8).y-rect_point)/2))), 1, (0, 0, 0), -1)
        # Mark the face landmarks with a circle
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
    # Reference time
    if flag == 1:
        start_time = time.time()
        prev_time = 0
        flag = 0

    end_time = time.time()
    elapsed_time = round((end_time-start_time),1)
    
    if elapsed_time - prev_time >= 0.5 and elapsed_time != prev_time:
        print(str(elapsed_time))
        line = []
        # Append current time to the list
        line.append(str(elapsed_time))
        for n in range(27, 68):
            # Get coordinates of landmarks
            point_x, point_y = norm_coord(landmarks.part(0).x, rect_point, landmarks.part(16).x, landmarks.part(8).y, landmarks.part(n).x, landmarks.part(n).y)
            # Append coordinates to the list
            line.append(str(point_x))
            line.append(str(point_y))
        # Append line to the CSV file
        with open('dane.csv', 'a', newline='') as new_file:
            writer = csv.writer(new_file, delimiter = ',')
            writer.writerow(line)

        prev_time = elapsed_time
    # Display frame
    cv2.imshow('Webcam Video', frame)
    # Exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()