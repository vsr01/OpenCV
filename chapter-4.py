import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#img[:] = 255,120,1

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,120,0),3)
cv2.rectangle(img,(0,0),(100,120),(0,100,180),2)
cv2.circle(img,(300,200),40,(0,200,100),2)
cv2.putText(img," Hello CV ",(100,400),cv2.FONT_HERSHEY_COMPLEX,0.4,(190,100,100),1)

cv2.imshow('Image',img)
cv2.waitKey(0)
