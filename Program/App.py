import cv2
import numpy

def height_conv (height):
    middle_height = 240
    new_height = middle_height - height
    return new_height

def width_conv (width):
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
    # Draw white pixel in the middle 
    mirror_frame[height_conv(2):height_conv(-2),width_conv(-2):width_conv(2)] = [0,0,255] 
    test = height_conv(20)
    # Display the frame
    cv2.imshow('Webcam Video',mirror_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ###print("Height: " + str(frame_height) + "\nWidth: " + str(frame_width))
        break

# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()