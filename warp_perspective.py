import cv2
import numpy as np

img = cv2.imread(".jpg")

width,height=250,350
part = np.float32([[111,219],[287,188],[154,482],[352,440]])
pers = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(part, pers)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image_original", img)
cv2.imshow("Image", imgOutput)
cv2.waitKey(0)