import cv2
from random import randrange

# Load pre-trained face detection data algorithm
trained_face_date = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load image to detect faces in
#img = cv2.imread('DT.jpg')   # Image with only one person
#img = cv2.imread('DTC2.jpg')   # Image with multiple persons

# To Capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over webcam frames
while True:

    ## Read the current frame
    successful_frame_read, frame = webcam.read()

    # Convert to grayscale
    gray_scaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_date.detectMultiScale(gray_scaled_img)

    # Draw rectangles
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0, 10))

    cv2.imshow('Miguel\'s Face Detector', frame)
    key = cv2.waitKey(1)

    ### Stop if Q key is pressed
    if key==81 or key==113:
        break

### Release the VideoCapture object
webcam.release()
"""
# Detect Faces
face_coordinates = trained_face_date.detectMultiScale(gray_scaled_img)

#print(face_coordinates)

# Draw rectangles around the face
#(x, y, w, h) = face_coordinates[0]
#cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


###You can load a different image with multiple people and they all will be detected,
    now im creating a for loop in case you wanna do that###

#for (x, y, w, h) in face_coordinates:
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 256, 0), 2)


###We can have randomly color for every person just need to import this at the top 
    from random import randrange, and then write a loop as
    ###

for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256), 10))




cv2.imshow('Miguel\'s Face Detector', img)
cv2.waitKey()
"""

print("Code Completed")













