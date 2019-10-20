"""

开闭操作
    开操作
    闭操作

开操作（Open）  尽量保留了其他元素没有变化   不同于模糊操作呢   可以提取水平的线或者竖直的线  就是还原插在字母里面的竖线和横线
    图像形态学的重要操作之一 基于膨胀与腐蚀操作组合形成的
    主要是应用在二值图像分析中 灰度图像亦可
    开操作 = 腐蚀 + 膨胀， 输入图像 + 结构元素
    可以去噪点呢

闭操作（Close）
    图像形态学的重要操作之一 基于膨胀与腐蚀操作组合形成的
    主要是应用在二值图像分析中 灰度图像亦可
    闭操作 = 膨胀 + 腐蚀， 输入图像 + 结构元素
    可以填充小的封闭区域呢


开闭操纵作用
    去除小的干扰快-----开操作
    填充闭合区域-------闭操作
    水平或者垂直线提取

"""


"""
开运算:先进性腐蚀再进行膨胀就叫做开运算,它被用来去除噪声。
闭运算:先膨胀再腐蚀。它经常被用来填充前景物体中的小洞，或者前景物体上的小黑点。
这里我们用到的函数是 cv2.morphologyEx()。
开闭操作作用：
1. 去除小的干扰块-开操作
2. 填充闭合区间-闭操作
3. 水平或垂直线提取,调整kernel的row，col值差异。
比如：采用开操作，kernel为(1, 15),提取垂直线，kernel为(15, 1),提取水平线，
"""


import cv2 as cv
import numpy as np


def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 可以提取水平(把第二个5换成1)的线(从左到右膨胀再腐蚀)或者竖直(把第一个5换成1)的线（从上向下腐蚀后再膨胀 一顿操作后又给修复了呢）
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)  # morphologyEx 形态学操作    cv.MORPH_OPEN 是 开操作形态学操作
    cv.imshow("open-result", binary)


def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)  # morphologyEx 形态学操作    cv.MORPH_CLOSE 是 开操作形态学操作
    cv.imshow("close-result", binary)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# open_demo(src)
close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
