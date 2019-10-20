"""

分水岭算法
    距离变换
    分水岭变换介绍
    OpenCV分水岭算法演示


距离变换(Distance Transform)
    一圈一圈的 由外向里marker(种子)越来越大


基于距离的分水岭分割流程！！！     融会贯通    ！！！
    输入图像->灰度->二值->距离变换->寻找种子->生成Marker->分水岭变换->输出图像->END



"""

import cv2 as cv
import numpy as np


def watershed_demo():
    # remove noise if any 
    print(src.shape)  # 图像的信息 高度和宽度 以及通道数
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)  # 边缘保留滤波 去噪的呢
    # gray/binary image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image ", binary)

    # morphology operation 形态学操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 结构元素
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)  # 连续两次进行开操作

    sure_bg = cv.dilate(mb, kernel, iterations=3)  # 膨胀操作

    cv.imshow("mor-opt", sure_bg)

    # distance transform
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)  # CV_DIST_L2（maskSize=3）是一个快速计算方法
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow("distance-t", dist_output*50)

    ret, surface = cv.threshold(dist, dist.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow("surface-bin", surface)

    surface_fg = np.uint8(surface)  # 为什么要转成uint8呢？
    unknown = cv.subtract(sure_bg, surface_fg)  # 为了着色做准备呢
    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)

    # watershed transform
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow("result", src)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/circle.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
watershed_demo()
cv.waitKey(0)
cv.destroyAllWindows()
