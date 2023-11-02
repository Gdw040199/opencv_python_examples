# 暴力匹配器、ORB描述符和match()方法
import cv2

img1 = cv2.imread("tester.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("finder.png", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck = False)
"""
bf = cv2.BFMatcher_create([normType[, crossCheck]])
bf为返回的暴力匹配器对象
normType为距离测量类型, 默认为cv2.NORM_L2, 通常, SIFT描述符使用cv2.NORM_L1或cv2.NORM_L2, ORB描述符使用cv2.NORM_HAMMING
crossCheck默认为False, 匹配器为每个查询描述符找到k个距离最近的匹配描述符, 为True时, 只返回满足交叉验证条件的匹配结果
"""
ms = bf.match(des1, des2)
ms = sorted(ms, key = lambda x:x.distance)
"""
ms = bf.match(des1, des2)
ms为返回的结果, 它是一个DMatch对象列表, 每个DMatch对象表示关键点的一个匹配结果, 其dintance属性表示距离, 距离值越小匹配度越高
des1为查询描述符
des2为训练描述符
"""
img3 = cv2.drawMatches(img1, kp1, img2, kp2, ms[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

"""
outImg = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2[, matchColor[, singlePointColor[, matchesMask[, flags]]]])
outImg = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches1to2[, matchColor[, singlePointColor[, matchesMask[, flags]]]])
outImg为返回的绘制结果图像, 图像中查询图像与训练图像中匹配的关键点个两点之间的连线为彩色
img1为查询图像
keypoints1为img1的关键点
img2为训练图像
keypoints2为img2的关键点
matches1to2为img1与img2的匹配结果
matchColor为关键点和链接线的颜色, 默认使用随机颜色
singlePointColor为单个关键点的颜色, 默认使用随机颜色
matchesMask为掩膜, 用于决定绘制哪些匹配结果, 默认为空, 表示绘制所有匹配结果
flags为标志, 可设置为下列参数值:
cv2.DrawMatchesFlags_DEFAUL:默认方式, 绘制两个源图像、匹配项和单个关键点, 没有围绕关键点的圆以及关键点的大小和方向
cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS:不会绘制单个关键点
cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS:在关键点周围绘制具有关键点大小和方向的圆圈
"""

cv2.imshow("tester", img1)
cv2.imshow("finder", img2)
cv2.imshow("matcher", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
