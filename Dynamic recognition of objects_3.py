import cv2
import numpy as np

images=cv2.imread('test_6.jpg')
gray=cv2.cvtColor(images,cv2.COLOR_BGR2GRAY)

template=gray[150:220,255:380]

match=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
locations=np.where(match>=0.9)

w,h=template.shape[0:2]
for p in zip(*locations[::-1]):
    x1,y1=p[0],p[1]
    x2,y2=x1+w,y1+h
    cv2.rectangle(images,(x1,y1),(x2,y2),(0,0,225),1)

cv2.imshow('image',images)
cv2.waitKey()

