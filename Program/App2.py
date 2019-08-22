import cv2
import numpy
import time

#Define frame size
frame_height = 540
frame_width = 960
# Initialize filter
face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')
# Initialize face coordinates
face_center = [0, 0]
prev_face_center = [0, 0]

# Height coordinates conversion 
def height_conv(height):
    global frame_height
    middle_height = frame_height/2
    new_height = middle_height - height
    return int(new_height)

# Width coordinates conversion
def width_conv(width):
    global frame_width
    middle_width = frame_width/2
    new_width = middle_width + width
    return int(new_width)

# Height coordinates conversion 2
def height_conv2(height):
    global frame_height
    middle_height = frame_height/2
    new_height2 = middle_height - height
    return int(new_height2)

# Width coordinates conversion 2
def width_conv2(width):
    global frame_width
    middle_width = frame_width/2 
    new_width2 = width - middle_width
    return int(new_width2)

# Capture video from deafult webcam
captured_video = cv2.VideoCapture(0)
captured_video.set(3, frame_width)
captured_video.set(4, frame_height)

while(True):
    # Obtain a frame from video and flip
    ret, frame = captured_video.read()
    frame = cv2.flip(frame, 1)
    # Draw a circle at [0, 0]
    frame = cv2.circle(frame, (width_conv(0), height_conv(0)), 3, (255, 255, 255), 1)
    # Convert frame to grey
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Face detection
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 4)
    # Draw rectangles around faces
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        face_center = [height_conv2(y+(h/2)), width_conv2(x+(w/2))]
    # Display the actual frame
    cv2.imshow('Webcam Video', frame)
    # Exit loop on key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()