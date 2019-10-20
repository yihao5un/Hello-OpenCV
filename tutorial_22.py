"""
图像的形态学
    膨胀
    腐蚀
    不仅支持二值的图像还支持彩色的图像
    相关API

图像形态学！！
是图像处理科学的一个单独分支学科
灰度与二值图像处理的重要手段
是由数学的集合论等相关理论得来的

膨胀(Dilate) 最大值滤波
3*3的结构元素/模板
    注意：
        腐蚀与膨胀都支持
        任意形状的结构元素
    作用：
    对像大小增加一个像素(3*3)
    平滑对象边缘
    减少(零距离接触)或者填充对象之间的距离


腐蚀(Erode)
    作用：
        对象大小减少一个像素
        平滑对象边缘
        弱化或者分割图像之间的半岛型连接
"""


import cv2 as cv
import numpy as np

# 腐蚀 就是越来越黑了
def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 结构元素 注意这个kernel 是 3*3的呢  越大的话  腐蚀的越严重
    dst = cv.erode(binary, kernel)
    cv.imshow("erode_demo", dst)


# 膨胀 就是把黑色变成白色的了
def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 结构元素 注意这个kernel 是 3*3的呢  越大的话  腐蚀的越严重
    dst = cv.dilate(binary, kernel)  # 腐蚀是dilate
    cv.imshow("dilate_demo", dst)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# erode_demo(src)
dilate_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()

