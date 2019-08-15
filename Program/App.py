import cv2
import numpy
import pyqtgraph
import time

#Define frame size
frame_height = 540
frame_width = 960
# Initialize filter
face_cascade = cv2.CascadeClassifier('C:\\Users\\cichy\\Desktop\\Praktyki_Folder\\haarcascade_frontalface_alt.xml')
# Initialize face coordinates
face_center = [0, 0]
prev_face_center = [0, 0]
# Initialize plotting data
w_data = []
h_data = []
t_data = []
# Get start time
start_time = time.time()

win = pyqtgraph.GraphicsWindow(title="Plots",size=(1900,1000))
width_plot = win.addPlot()
height_plot = win.addPlot()

width_curve = width_plot.plot()
height_curve = height_plot.plot()

width_plot.setYRange(-frame_width/2,frame_width/2)
height_plot.setYRange(-frame_height/2,frame_height/2)

width_plot.showGrid(x=False, y=True)
height_plot.showGrid(x=False, y=True)

width_plot.addLegend()
height_plot.addLegend()

width_plot.setLabel('left', 'Width', units='px')
width_plot.setLabel('bottom', 'Time', units='s')
height_plot.setLabel('left', 'Height', units='px')
height_plot.setLabel('bottom', 'Time', units='s')



def update():
    global w_data, h_data, t_data
    width_curve.setData(t_data, w_data, pen="b")
    height_curve.setData(t_data, h_data, pen="r")

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
    # Draw rectangles around faces, circle in the middle, print coordinates
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 1)
        face_center = [height_conv2(y+(h/2)), width_conv2(x+(w/2))]
        frame = cv2.circle(frame, (int(x+(w/2)), int(y+(h/2))), 3, (255,0,0), 1)
        end_time = time.time()
        h_data.append(face_center[0])
        w_data.append(face_center[1])
        t_data.append(end_time-start_time)
    # Display the actual frame
    print("Height: " + str(face_center[0]) + " Width: " + str(face_center[1]))
    frame = cv2.line(frame, (width_conv(face_center[1]), height_conv(face_center[0])), (width_conv(prev_face_center[1]), height_conv(prev_face_center[0])), (0, 255, 0), 1)
    cv2.imshow('Webcam Video', frame)
    # Update plots
    update()
    prev_face_center = face_center
    # Exit loop on key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Height: " + str(frame_height) + "\nWidth: " + str(frame_width))
        break
# Release the webcam and close window
captured_video.release()
cv2.destroyAllWindows()