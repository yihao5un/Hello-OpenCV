"""
直线检测：
霍夫直线变换介绍（前提是边缘检测已经完成）  先是由直坐标到极坐标 再由 极坐标还原到直坐标
    来自于直线坐标和极坐标的转换
    Hough Line Transform 用来做直线检测
    前提条件-边缘检测已经完成
    平面空间到极坐标空间转换

关于霍夫变换的相关知识可以看看这个博客：https://blog.csdn.net/kbccs/article/details/79641887

相关API代码演示

"""


import cv2 as cv
import numpy as np


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)  # 窗口大小为3
    # cv2.HoughLines()返回值就是（ρ,θ）。ρ 的单位是像素，θ 的单位是弧度。
    # 这个函数的第一个参数是一个二值化图像，所以在进行霍夫变换之前要首先进行二值化，或者进行 Canny 边缘检测。
    # 第二和第三个值分别代表 ρ 和 θ 的精确度。第四个参数是阈值，只有累加其中的值高于阈值时才被认为是一条直线，
    # 也可以把它看成能 检测到的直线的最短长度（以像素点为单位）。
    lines = cv.HoughLines(edges, 1, np.pi/180, 200)  # 变成 极坐标的点
    for line in lines:
        print(type(lines))
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))  # 只有看源码才能知道为什么乘以1000
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image-lines", image)


def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)  # 自动检测   注意参数minLineLength=50, maxLineGap=10什么意思
    for line in lines:
        print(type(line))
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("line_detect_possible_demo", image)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/image_lines.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# line_detection(src)
line_detect_possible_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
