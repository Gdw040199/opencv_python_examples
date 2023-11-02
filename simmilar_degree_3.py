import cv2
import numpy as np 
import math

def PSNR(img1, img2):
    mse = np.mean((img1/255. - img2/255.) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 1
    return 20 * math.log(PIXEL_MAX / math.sqrt(mse),10)


def main():
    img1 = cv2.imread(r'Thumbnails_0.jpeg')
    img2 = cv2.imread(r'Thumbnails_1.jpeg')
    n = PSNR(img1, img2)
    print('PSNR算法相似度:', n)

if __name__=="__main__":
    main()
