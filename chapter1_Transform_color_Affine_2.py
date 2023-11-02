import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('test_4.png')

#缩放图像
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
# #OR
# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#################################
#cv2.resize(InputArray src, OutputArray dst, Size, fx, fy, interpolation)
#参数说明：
#nputArray src	输入图片
#OutputArray dst	输出图片
#Size	输出图片尺寸
#fx, fy	沿x轴，y轴的缩放系数
#interpolation	插入方式
#1.参数三size与参数四fx，fy可以二选一
#2.参数五interpolation：在缩放时我们推荐使用 cv2.INTER_AREA， 在扩展时我们推荐使用 v2.INTER_CUBIC（慢) 和 v2.INTER_LINEAR。 默认情况下所有改变图像尺寸大小的操作使用的插值方法都是 cv2.INTER_LINEAR
##############################################
cv2.imshow("img", img)
cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#平移图像
height,width=img.shape[0:2]
imgShift = np.float32([[1,0,100],[0,1,200]])# [1,0,100]的意思是，宽右移距离100 [0,1,200]高下移200 #变换矩阵
dst = cv2.warpAffine(img,imgShift,(width,height))
cv2.imshow('img_translate',dst)
cv2.waitKey(0)
################################################
#使用numpy数组构建移动矩阵(np.float32) 然后传入cv2.warpAffine()函数
#cv2.warpAffine(src, M, dsize,dst,flags,borderMode,borderValue) → dst
#参数说明：
#src 输入图像
#M	换矩阵，一般反映平移或旋转的关系，为InputArray类型的2×3变换矩阵。
#dszie	输出图像的大小
#flags	插值方法的组合（int 类型）
#borderMode	边界像素模式（int 类型）
#borderValue  	边界填充值; 默认情况下，它为0，也就是边界填充默认是黑色。
#其中flags表示插值方式，有以下取值
#cv2.INTER_LINEAR	线性插值(默认)
#cv2.INTER_NEAREST	最近邻插值
#cv2.INTER_AREA	区域插值
#cv2.INTER_CUBIC	三次样条插值
#cv2.INTER_LANCZOS4	Lanczos插值
##################################################

#图像旋转
#在不缩放的情况下将图像旋转 90 度
height,width=img.shape[0:2]
M=cv2.getRotationMatrix2D((height/2,width/2),90,1)
dst=cv2.warpAffine(img,M,(width,height))
cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
#################################################
#为了构建这个旋转矩阵，OpenCV 提供了一个函数：cv2.getRotationMatrix2D。 下面的例子是在不缩放的情况下将图像旋转 90 度。
#因此要实现对一个图像进行旋转操作，就需要先通过cv2.getRotationMatrix2D函数获取旋转矩阵，再使用cv2.warpAffine函数进行旋转变换
#获取旋转矩阵函数：M=cv2.getRotationMatrix2D(center, angle, scale)
#参数说明：
#center	图片的旋转中心
#angle	旋转角度
#scale	旋转后图像相比原来的缩放比例
#M	计算得到的旋转矩阵


#仿射变换
rows,cols,ch = img.shape
pts1 = np.float32([[20,20],[110,20],[50,110]]) #三个原来点的坐标
pts2 = np.float32([[10,50],[120,40],[30,150]]) #仿射变换后这三个点的坐标
#使用np.float32构建2x3矩阵，然后传入cv2.getAffineTransform()函数构建变换矩阵
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

##################################
#在仿射变换中，原图中所有的平行线在结果图像中同样平行。为了创建这个矩阵我们需要从原图像中找到三个点以及他们在输出图像中的位置。
#然后 cv2.getAffineTransform 会创建一个 2x3 的矩阵，最后这个矩阵会被传给 函数 cv2.warpAffine。
#函数：M=cv2.GetAffineTransform(src, dst)
#参数说明：
#src	原始图像中的三个点的坐标
#dst	变换后的这三个点对应的坐标
#M	根据三个对应点求出的仿射变换矩阵
#################################









