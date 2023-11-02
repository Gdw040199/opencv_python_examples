import cv2
from PIL import Image
color_image=cv2.imread('bird.png')
cv2.imshow('original image',color_image)
gray_image=cv2.cvtColor(color_image,cv2.COLOR_RGB2GRAY)
gray=Image.fromarray(gray_image)
gray.save('gray.png')
cv2.imshow('Gray Image',gray_image)
cv2.waitKey(0)