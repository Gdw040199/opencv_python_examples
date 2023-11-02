# 暴力匹配器、ORB描述符和knnMatch()方法
import cv2

img1 = cv2.imread("tester.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("finder.png", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck = False)
ms = bf.knnMatch(des1, des2, k=2)
"""
ms = knnMatch(des1, des2, k=n)
ms为返回的匹配结果, 每个列表元素是一个子列表, 它包含了由参数k指定个数的DMatch对象
des1为查询描述符
des2为训练描述符
k为返回的最佳匹配个数
"""

# 应用比例测试选择要使用的匹配结果
good = []
for m, n in ms:
    if m.distance < 0.75 * n.distance:
        good.append(m)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, good[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# good = np.expand_dims(good,1)
#img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:20], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow("tester", img1)
cv2.imshow("finder", img2)
cv2.imshow("Matcher", img3)


cv2.waitKey(0)
cv2.destroyAllWindows()
