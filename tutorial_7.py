import cv2 as cv
import numpy as np


def clamp(pv):  # 为了防止溢出错误
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    h, w, c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)  # 产生随机数
            b = image[row, col, 0]  # blue
            g = image[row, col, 1]  # green
            r = image[row, col, 2]  # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise image", image)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# t1 = cv.getTickCount()
# gaussian_noise(src)
# t2 = cv.getTickCount()
# time = (t2-t1)/cv.getTickFrequency()
# print("时间消耗: %s" % (time * 1000) + " ms")
dst = cv.GaussianBlur(src, (0, 0), 15)  # 高斯窗口是（0，0） 后面那个15 表示模糊的程度 越大表示 越模糊

# 关于参数ksize：
#
# ksize.width和ksize.height可以不同
# 取值有2种情况：
# 可以是正的奇数
# 也可以是0，此时它们的值会自动由sigma进行计算
# 关于参数sigmaX和sigmaY：
#
# sigmaY=0时，其值自动由sigmaX确定（sigmaY=sigmaX）；
# sigmaY=sigmaX=0时，它们的值将由ksize.width和ksize.height自动确定；

cv.imshow("Gaussian Blur", dst)
cv.waitKey(0)

cv.destroyAllWindows()
