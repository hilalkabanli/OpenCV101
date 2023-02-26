import cv2

img=cv2.imread("Resources/gogh.jpg")
print(img.shape)

imgResize=cv2.resize(img,(300,200))#width and then height

cv2.imshow("resize",imgResize)

#cropping
imgCropped=img[0:200,800:1000]
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)