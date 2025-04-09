# OpenCV program to detect face in real time
# import libraries of python OpenCV 
# where its functionality resides
import cv2 

# load the required trained XML classifiers
# https://github.com/Itseez/opencv/blob/master/
# data/haarcascades/haarcascade_frontalface_default.xml
# Trained XML classifiers describes some features of some
# object we want to detect a cascade function is trained
# from a lot of positive(faces) and negative(non-faces)
# images.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# https://github.com/Itseez/opencv/blob/master
# /data/haarcascades/haarcascade_eye.xml
# Trained XML file for detecting eyes
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')



# capture frames from a camera
cap = cv2.VideoCapture(0)

colors = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "yellow": (0, 255, 255),
    "cyan": (255, 255, 0),
    "magenta": (255, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
}
color = 0

# loop runs if capturing has been initialized.
while 1: 
    current_color = list(colors.values())[color]
    next_color = list(colors.values())[(color + 1) % len(colors)]
 
    # reads frames from a camera
    ret, img = cap.read() 
    

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    profile = profile_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.putText(img, "Face", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, current_color, 2)
        # To draw a rectangle in a face 
        cv2.rectangle(img,(x,y),(x+w,y+h),current_color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray) 

        #To draw a rectangle in eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.putText(roi_color, "Eye", (ex, ey-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, next_color, 2)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),next_color,2)
            
    """ for (x,y,w,h) in profile:
        cv2.putText(img, "Profile", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, current_color    , 2)
        # To draw a rectangle in a face 
        cv2.rectangle(img,(x,y),(x+w,y+h),current_color,2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w] """

    # Display an image in a window
    cv2.imshow('img',img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == 32: 
        color = (color + 1) % len(colors)
        print(color)
        

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows() 