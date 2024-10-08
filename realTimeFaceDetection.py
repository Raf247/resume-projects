import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#acces the webcam
video_capture = cv2.VideoCapture(0)

#function to detect faces
def detect_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize = (40,40))
    for(x,y,w,h) in faces:
        cv2.rectangle(vid,(x,y), (x + w, y + h), (0,255,0), 4)
    return faces

#loop for real-time detection
while True:
    result, video_frame = video_capture.read() 
    if result is False:
        break

    faces = detect_box(video_frame)

    cv2.imshow("Face Detection Project", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()