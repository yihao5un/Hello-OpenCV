"""
图像梯度
一阶导数与Soble算子 (对噪声比较敏感)
    图像边缘 也就是导数最大的地方(最抖的地方)

二阶导数与拉普拉斯算子
    求二阶导数
    算子加起来是0
"""


import cv2 as cv
import numpy as np


def soble_demo(image):
    # Scharr 算子 是Soble算子的增强版本  更加清晰
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)  # 在x方向 左右有差异的全部表示出来
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)  # 在y方向 上下有差异的全部表示出来
    gradx = cv.convertScaleAbs(grad_x)  # 转成绝对值
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)  # 算出整个   # 计算两个图像的权值和，dst = src1*alpha + src2*beta + gamma
    cv.imshow("gradient", gradxy)


def lapalian_demo(image):
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    # 手动定义一个
    # kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])  # 定义一个lpls算子kernel 4领域默认的
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])  # 定义一个lpls算子kernel 8领域
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)  # 变成单通道的呢  # 由于算完的图像有正有负，所以对其取绝对值
    cv.imshow("lapalian_demo", lpls)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# soble_demo(src)
lapalian_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
