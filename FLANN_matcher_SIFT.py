# FLANN匹配器、SIFT描述符
import cv2

img1 = cv2.imread("tester.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("finder.png", cv2.IMREAD_GRAYSCALE)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# 定义FLANN参数
FLANN_INDEX_KDTREE = 1
#FLANN
index_params = dict(algorithm = FLANN_INDEX_KDTREE,
                    trees = 5)
search_params = dict(check = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.match(des1, des2)
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = None,
                   flags = cv2.DrawMatchesFlags_DEFAULT)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], None, **draw_params)

cv2.imshow("tester", img1)
cv2.imshow("finder", img2)
cv2.imshow("Matches", img3)


cv2.waitKey(0)
cv2.destroyAllWindows()
