import cv2
import numpy


frame_height = 0
frame_width = 0
face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')

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
    new_height = middle_height - height
    return int(new_height)

# Width coordinates conversion 2
def width_conv2(width):
    global frame_width
    middle_width = frame_width/2 
    new_width = width - middle_width
    return int(new_width)

# Capture video from deafult webcam
captured_video = cv2.VideoCapture(0)
captured_video.set(3, 960)
captured_video.set(4, 540)

while(True):
    # Obtain a frame from video and flip
    ret, frame = captured_video.read()
    mirror_frame = cv2.flip(frame, 1)
    # Get frame size
    frame_height = numpy.size(mirror_frame, 0)
    frame_width = numpy.size(mirror_frame, 1)
    # Draw circle at [0, 0]
    mirror_frame = cv2.circle(mirror_frame, (width_conv(0), height_conv(0)), 3, (0,0,255), 1)
    # Convert frame to grey
    gray_frame = cv2.cvtColor(mirror_frame, cv2.COLOR_BGR2GRAY)
    # Face detection
    faces = face_cascade.detectMultiScale(gray_frame)
    # Draw rectangles around faces, circle in the middle, print coordinates
    for (x,y,w,h) in faces:
        mirror_frame = cv2.rectangle(mirror_frame, (x,y), (x+w,y+h), (0,0,255), 1)
        face_middle = [height_conv2(y+(h/2)), width_conv2(x+(w/2))]
        print("Height: " + str(face_middle[0]) + " Width: " + str(face_middle[1]))
        mirror_frame = cv2.circle(mirror_frame, (int(x+(w/2)), int(y+(h/2))), 3, (0,255,0), 1)
    # Display the frame
    cv2.imshow('Webcam Video', mirror_frame)
    # Exit loop on key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Height: " + str(frame_height) + "\nWidth: " + str(frame_width))
        break

# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()