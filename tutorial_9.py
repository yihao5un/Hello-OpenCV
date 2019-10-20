"""

图像直方图(Histogram)

"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])  # ravel() 统计出现的次数 将图像展开 256是bins数 范围是0-256
    plt.show()


def image_hist(image):  # 主要是找图像的最高的地方 越往左越黑 越往右越白
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
        # 计算出直方图，calcHist(images, channels, mask, histSize(有多少个bin), ranges[, hist[, accumulate]]) -> hist
        # hist 是一个 256x1 的数组，每一个值代表了与该灰度值对应的像素点数目。
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

 
print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
image_hist(src)
cv.waitKey(0)

cv.destroyAllWindows()
