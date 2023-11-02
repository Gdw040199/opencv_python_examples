#导入必要的软件包
import cv2

#从磁盘加载输入图像和模板图像，然后显示在我们的屏幕上
print("[INFO] loading images...")
image = cv2.imread("test_7.png")
template = cv2.imread("template.png")
cv2.imshow("Image", image)
cv2.imshow("Template", template)
#将图像和模板都转换为灰度
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

#执行模板匹配
print("[INFO] performing template matching...")
result = cv2.matchTemplate(imageGray, templateGray,	cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

#确定起点和终点的(x，y)坐标边界框
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

#在图像上绘制边框
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)
#显示输出图像
cv2.imshow("Output", image)
cv2.waitKey(0)



