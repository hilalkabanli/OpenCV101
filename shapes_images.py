import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[300:400]=255,0,0
#cv2.imshow("image",img)

#slash
cv2.line(img,(0,0),(300,300),(0,255,0),3)#300,300 matrixine gelene kadar
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)#width first then height
#cv2.imshow("Image",img)

#rectangle and circle
#cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)#2 is thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5)#30 is raadius, color, thickness
#cv2.imshow("Image",img)

#putText                                                     #1 is scale
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.imshow("Image",img)

cv2.waitKey(0)