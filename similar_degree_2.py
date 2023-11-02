import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib.pyplot as plt
import seaborn as sns
 
def classify_with_split(image1, image2):
    npart = 10
    #每张图片分割成10x10份
    hd1,wd1 = image1.shape[0]/npart,image1.shape[1]/npart
    hd2,wd2 = image2.shape[0]/npart,image2.shape[1]/npart
    #分别算每张割片的hash值
    hash_arr1 = np.zeros((npart,npart,100))
    hash_arr2 = np.zeros((npart,npart,100))
    #第二张图片的第1张割片，去匹配第一张图片的所有割片，并创建热力图
    match_arr =  np.zeros((npart,npart))
    for i1 in range(0,npart):
        for j1 in range(0,npart):
            p_img1 = image1[round(i1*hd1):round((i1+1)*hd1) , round(wd1*j1):round(wd1*(j1+1))]
            p_img2 = image2[0:round(hd2) , 0:round(wd2)]
            ssimRate = compare_ssim(p_img1, p_img2, multichannel=True)
            match_arr[i1,j1]=ssimRate
            #print("[%d,%d]vs[%d,%d]=%.2f"%(0,0,i1,j1,ssimRate))
    #print(match_arr)
    #绘图
    f, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(match_arr, ax=ax,cmap='YlOrRd',linewidths=0.1,linecolor="grey",cbar_kws={"orientation":"horizontal"})
 
    plt.savefig(r"ssim.png",dpi=75)
    plt.show()
    pos_max = np.unravel_index(np.argmax(match_arr),match_arr.shape)
    #print(pos_max)
    rate = (npart-pos_max[0])*(npart-pos_max[1])/(npart * npart)
    return rate
 
def main():
    img1 = cv2.imread(r'Thumbnails_0.jpeg')
    img2 = cv2.imread(r'Thumbnails_1.jpeg')
    n = classify_with_split(img1, img2)
    print('ssim算法相似度:', n)
 
 
if __name__=="__main__":
    main()

