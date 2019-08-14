import cv2
import numpy

face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')

# Height coordinates conversion
def height_conv(height):
    middle_height = 240
    new_height = middle_height - height
    return new_height

# Width coordinates conversion
def width_conv(width):
    middle_width = 320
    new_width = middle_width + width
    return new_width


# Capture video from deafult webcam
captured_video = cv2.VideoCapture(0)

while(True):
    # Obtain a frame from video and flip
    ret, frame = captured_video.read()
    mirror_frame = cv2.flip(frame,1)
    # Get frame size
    frame_height = numpy.size(mirror_frame, 0)
    frame_width = numpy.size(mirror_frame, 1)
    # Draw red square at [0,0]
    mirror_frame[height_conv(2):height_conv(-2),width_conv(-2):width_conv(2)] = [0, 0, 255] 

    gray_frame = cv2.cvtColor(mirror_frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame)
    for (x,y,w,h) in faces:
        mirror_frame = cv2.rectangle(mirror_frame,(x,y),(x+w,y+h),(0,0,255),1)

    # Display the frame
    cv2.imshow('Webcam Video',mirror_frame)
    # Exit loop on key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Height: " + str(frame_height) + "\nWidth: " + str(frame_width))
        break

# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()