import cv2, time

video = cv2.VideoCapture(0) #Video capture object and 0 tells python to use my default webcam
face_cascade = cv2.CascadeClassifier("C:\\Users\\Tobi\\Documents\\Ubiqum Course Docs 2019\\Ubiqum_Experience\\OpenCV\\openCV_libs\\haarcascade_frontalface_default.xml")

a = 1
while True:

    a = a+1
    #'Check' is a boolean datatype and will return True if Python is able to read from the video output
    #'Frame' is a numpy array which prints the first frame(screenshot) from the video capture
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05,
                                        minNeighbors=5)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    #Write text on top of video feed
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Face Detection',(100,450), font, 2,(255,255,255),2,cv2.LINE_AA)

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1) #this will generate a new frame after every 1 second

    #Will destry window once 'q' is entered
    if key == ord('q'):  
        break

print(a) #This will print the number of frames
#time.sleep(3)
print("Faces is: ",faces.shape[0])
#cv2.imshow("Capturing", frame)


video.release()

cv2.destroyAllWindows()
