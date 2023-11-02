import numpy as np
from skimage.io import imread
import skiamge.color #import rgb21ab,lab2rgb
import cv2
import matplotlib.pylab as plt
im=imread('bird.png')
im1=rgb21ab(im)
im1[...,1]=im1[...,2]=0
im1=lab2rgb(im1)
plt.figure(figsize=(20,10))
plt.subplot(121),plt.imshow(im),plt.axis('off')
plt.title('Original image',size=20)
plt.subplot(122),plt.imshow(im1),plt.axis('off'),plt.title('Grayscale image',size=20)
