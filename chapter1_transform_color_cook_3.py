import cv2
import numpy as np
import matplotlib.pyplot as plt
 
def imgBrightness(img1, c, b): 
    rows, cols, channels = img1.shape
    blank = np.zeros([rows, cols, channels], img1.dtype) #生成满足图片矩阵大小的空白矩阵
    #shape：创建的新数组的形状（维度）。
    #dtype：创建新数组的数据类型。
    #返回值：给定维度的全零数组
    rst = cv2.addWeighted(img1, c, blank, 1-c, b) 
    #函数cv2.addWeighted（）的主要功能就是将两幅图像合成为一幅图像 ，但是由于blank是空的而且大小和原图相同，所以就可以
    #而第二个，第四个和第五个参数是ɑ，β，γ 分别是alpha: 第一幅图像的权重(取值范围为 0 到 1)beta: 第二幅图像的权重(取值范围为 0 到 1)gamma: 求和后的偏移量
    return rst #返回生成的图片
img = cv2.imread('test_2.png')
dst = imgBrightness(img, 0.8, 0) #变暗
dst2 = imgBrightness(img, 1.2, 0) #变亮
 
cv2.namedWindow("origin",0)
cv2.resizeWindow("origin", 1223, 500)# 高*宽，改变窗口大小
cv2.imshow('origin',img)
 
cv2.namedWindow("enhanced",0)
cv2.resizeWindow("enhanced", 1223, 500)
cv2.imshow('enhanced',dst)
 
cv2.namedWindow("enhanced2",0)
cv2.resizeWindow("enhanced2", 1223, 500)
cv2.imshow('enhanced2',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁/关闭所有窗口

 

 
