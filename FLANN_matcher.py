# FLANN匹配器、ORB描述符
import cv2

img1 = cv2.imread("tester.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("finder.png", cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 定义FLANN参数
"""
在创建FLANN匹配器时,需要传递两参数:index_params和search_params。
index_params用来指定索引树的算法类型和数量。SIFT算法可以使用下面的代码来设置
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE,
                    trees= 5)
ORB算法可以使用下面的代码来设置。
FLANN_INDEX_LSH = 6
index_params = dict(algorithm = FLANN_INDEX_LSH,
                    table_number = 6,
                    key_size = 12,
                    multi_probe_level = 1)          
"""
FLANN_INDEX_LSH = 6
#ORB
index_params = dict(algorithm = FLANN_INDEX_LSH,
                    table_number = 6,
                    key_size = 12,
                    multi_probe_level = 1)
search_params = dict(check = 50)
#search_params用于指定索引树的遍历次数，遍历次数越多，匹配结果越精细，通常设置为50即可，如上所示：

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
