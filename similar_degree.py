# -*- coding: utf-8 -*-
import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib.pyplot as plt
 
# 通过得到RGB每个通道的直方图来计算相似度
def classify_hist_with_split(image1, image2):
    # 将图像分离为RGB三个通道，再计算每个通道的相似值
    arr_image1 = cv2.split(image1)
    arr_image2 = cv2.split(image2)
    sub_data = 0
    npart = 10  #纵向分割
    x_arr = [i for i in range(npart)]#np.arange(npart)
    y1_arr = []
    y2_arr = []
    y3_arr = []
    wp1,wp2 = image1.shape[1]/npart,image2.shape[1]/npart
    h_img2 = arr_image2[0][:,0:round(wp2)]  #第二张图片的第一通道的第1片
    for i in range(0,npart):   #循环对比第一张图片
        h_img1 = arr_image1[0][:,round(wp1*i):round(wp1*(i+1))]
        idata = calculate(h_img2,h_img1)
        y1_arr.append(idata)
        print(idata)
    print("-----------")
    max1_index = y1_arr.index(max(y1_arr))
    h_img2 = arr_image2[1][:,0:round(wp2)]  #第二张图片的第二通道的第1片
    for i in range(0,npart):   #循环对比第一张图片
        h_img1 = arr_image1[1][:,round(wp1*i):round(wp1*(i+1))]
        idata = calculate(h_img2,h_img1)
        y2_arr.append(idata)
        print(idata)
    print("-----------")
    max2_index = y2_arr.index(max(y2_arr))
    h_img2 = arr_image2[2][:,0:round(wp2)]  #第二张图片的第三通道的第1片
    for i in range(0,npart):   #循环对比第一张图片
        h_img1 = arr_image1[2][:,round(wp1*i):round(wp1*(i+1))]
        idata = calculate(h_img2,h_img1)
        y3_arr.append(idata)
        print(idata)
    max3_index = y3_arr.index(max(y3_arr))
    #plt.plot(x_arr,y1_arr,"r:x")
    plt.plot(x_arr,y1_arr,"r:x",
             x_arr,y2_arr,"b-D",
             x_arr,y3_arr,"y--_")
    plt.savefig(r"c123.png",dpi=75)
    plt.show()
    print("-----------")
    print("%d,%d,%d" % (max1_index,max2_index,max3_index))
    sub_data = (max1_index+max2_index+max3_index+3)/(npart*3)
    return sub_data
# 计算单通道的直方图的相似值
def calculate(image1, image2):
    hist1 = cv2.calcHist([image1], [0], None, [256], [0.0, 255.0])
    hist2 = cv2.calcHist([image2], [0], None, [256], [0.0, 255.0])
    # 计算直方图的重合度
    degree = 0
    for i in range(len(hist1)):
        if hist1[i] != hist2[i]:
            degree = degree + (1 - abs(hist1[i] - hist2[i]) / max(hist1[i], hist2[i]))
        else:
            degree = degree + 1
    degree = degree / len(hist1)
    return degree
def main():
    img1 = cv2.imread(r'Thumbnails_0.jpeg')
    img2 = cv2.imread(r'Thumbnails_1.jpeg')
    n = classify_hist_with_split(img1, img2)
    print('三色直方图算法相似度：', n)
 
 
if __name__=="__main__":
    main()

