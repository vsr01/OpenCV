import cv2

img = cv2.imread('lambo.png')
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200,200:500]
print(imgCropped.shape)

cv2.imshow('Image',img)
cv2.imshow('Resized Image',imgResize)
cv2.imshow('Cropped Image',imgCropped)
cv2.waitKey(0)
