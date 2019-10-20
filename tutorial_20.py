"""
轮廓发现
基于二值图像 基于图像边缘提取的基础寻找对象轮廓的方法
所以边缘提取的阈值选定会影响最终轮廓发现结果

"""


import cv2 as cv
import numpy as np


"""Canny边缘提取"""


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # blur可以降低噪声
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # x gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)  # 注意不能是浮点数 应该是CV_16SC1
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    # 求边缘
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 低阈值是50 高阈值150 是3倍的
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    return edge_output

# 轮廓发现
def contours_demo(image):
    """
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 得到二值图像
    cv.imshow("binary image", binary)
    """

    binary = edge_demo(image)
    # contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  # 最主要的是 contours
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # cv.RETR_EXTERNAL 之后就不包括硬币里面的了 直接搞外层的了
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)  # 如果把2 换成-1 那么就把 硬币 里面给填充了
        print(i)
    cv.imshow("detect contours", image)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
