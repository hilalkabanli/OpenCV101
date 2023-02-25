import cv2
#image
img = cv2.imread("Resources/gogh.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)
#show video
cap = cv2.videocapture("Resources/.mp4")
while true:
    success, imgv =cap.read()
    cv2.imshow("video", imgv)
    if cv2.waitkey(1) & 0xff == ord('q'):
        break
#open webcam
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)
webcam.set(10,100)#brightness
while True:
    success, img2 = webcam.read()
    cv2.imshow('Video',img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


