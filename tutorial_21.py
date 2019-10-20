"""
对象检测
    弧长与面积
    对边形拟合
    几何矩计算
    相关API代码

弧长与面积：轮廓发现 像素为单位
多边形拟合：approxPolyDP
几何矩的计算：原点矩和中心矩 以及图像重心坐标

"""


import cv2 as cv
import numpy as np


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 二值化 阈值  INV 是取反的意思
    print("threshold value : %s" % ret)
    cv.imshow("binary image", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # 找到轮廓
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)  # 计算轮廓面积
        x, y, w, h = cv.boundingRect(contour)  # 用矩阵框出轮廓

        rate = min(w, h)/max(w, h)   # 宽高比例  1数字 的 比例最小
        print("rectangle rate : %s" % rate)

        mm = cv.moments(contour)  # 计算几何矩
        print(type(mm))  # 是字典类型
        # 计算出对象的重心
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 2, (0, 255, 255), -1)  # 重心位置为为黄色
        # cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print("contour area %s" % area)  # 注意 中间不用加逗号的呢  将每一个字的面积计算出来





        # 将轮廓形状近似到另外一种由更少点组成的轮廓形状，新轮廓的点的数目由我们设定的准确度来决定。
        # 为了帮助理解，假设从一幅图像中查找一个矩形，但是由于图像的种种原因，我们不能得到一个完美的矩形，
        # 而是一个“坏形状”（如下图所示）。
        # 现在你就可以使用这个函数来近似这个形状（）了。
        # 这个函数的第二个参数叫 epsilon，它是从原始轮廓到近似轮廓的最大距离。
        # 它是一个准确度参数。选 择一个好的 epsilon 对于得到满意结果非常重要。
        approxCurve = cv.approxPolyDP(contour, 4, True)  # 多边形矩形逼近
        # 轮廓周长,第二参数可以用来指定对象的形状是闭合的（True）,还是打开的（一条曲线）。
        print(approxCurve.shape)
        if approxCurve.shape[0] > 10:  # 圆的范围
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCurve.shape[0] == 4:  # 矩形的范围
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
        if approxCurve.shape[0] == 3:  # 三角形的范围
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
    cv.imshow("measure-contours", dst)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/handwriting.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
measure_object(src)
cv.waitKey(0)
cv.destroyAllWindows()
