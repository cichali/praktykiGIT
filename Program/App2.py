import cv2
import dlib
import time
import numpy

#Define frame size
frame_height = 540
frame_width = 960
# Initialize filter
face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')
# Initialize face coordinates
face_center = [0, 0]
prev_face_center = [0, 0]

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\shape_predictor_68_face_landmarks.dat")


# Capture video from deafult webcam
captured_video = cv2.VideoCapture(0)
captured_video.set(3, frame_width)
captured_video.set(4, frame_height)

#frame_width = frame_height

def norm_x(x):
    x = float(x)
    new_x = (x-(frame_width/2))/(frame_width/2)
    return(new_x)

def norm_y(y):
    y = float(y)
    new_y = (y-(frame_height/2))/(-frame_height/2)
    return(new_y)

while(True):
    # Obtain a frame from video and flip
    ret, frame = captured_video.read()
    frame = cv2.flip(frame, 1)
    # crop frame to square
    ###frame = frame[0:720, int((frame_width-frame_height)/2):int(frame_width-(frame_width-frame_height)/2)]
    # Draw a circle at [0, 0]
    cv2.circle(frame, (int(frame_width/2), int(frame_height/2)), 2, (0, 0, 255), 1)
    ### frame = cv2.circle(frame, (TU DAJ X,TU DAJ Y , 3, (255, 255, 255), 1)
    # Convert frame to grey
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Face detection
    faces = detector(gray_frame)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        landmarks = predictor(gray_frame, face)

        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            print(str(norm_x(landmarks.part(30).x)) + ", " + str(norm_y(landmarks.part(30).y)))

    # Display the actual frame
    cv2.imshow('Webcam Video', frame)
    height = frame.shape[0]
    width = frame.shape[1] 
    # Exit loop on key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(str(width) + ", " + str(height))
        break
# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()