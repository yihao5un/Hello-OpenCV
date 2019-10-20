"""

图像金字塔
1.高斯金字塔
reduce =  高斯模糊 + 降采样
取偶数行和偶数列
需要一层一层的
expend = 扩大 + 卷积

2.拉普拉斯金字塔
L1 = g1 - expand(g2)

PyrDown:降采样
PyrUp:还原
高斯金字塔与拉普拉斯金字塔

"""
import cv2 as cv
import numpy as np


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)  # reduce 过程
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_" + str(i), dst)
        temp = dst.copy()  # 经过一次reduce 之后的图片
    return pyramid_images  # 返回图像的列表


def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)  # 用高斯金字塔的返回结果
    level = len(pyramid_images)  # 计算出有多少层
    for i in range(level-1, -1, -1):
        if i-1 < 0 :  # 判断最后一个
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])  # image 是原图
            lpls = cv.subtract(image, expand)  # 公式：L1 = g1 - expand(g2))
            cv.imshow("lapalian_down_" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")  # 我这个图片不可以 应该必须是2的n次方的图片大小才行0
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
