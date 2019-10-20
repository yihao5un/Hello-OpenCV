"""
圆检测
    霍夫圆检测原理
    从平面坐标到极坐标转换三个参数C(x0, y0, r)其中x0,y0是圆心，假设平面坐标的任意一个圆上的点 转移到极坐标中C(x0,y0,r) 处有最大值 也就是最亮的地方 霍夫变换正是利用这个原理实现圆的检测的
    现实考量
    因为对噪声比较敏感 多以首先要对图像中值滤波
    分为两步：
    1.检测边缘 发现可能圆心
    2.基于第一步从候选圆心开始计算最佳半径大小

    代码层面知识点

"""
import cv2 as cv
import numpy as np


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)  # 边缘保留滤波  必须略去噪生  要不就变乱了
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  # 画出圆
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)  # 画出圆心
    cv.imshow("circles", image)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
