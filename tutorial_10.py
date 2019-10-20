"""
直方图应用->直方图均衡化(基于灰度图像的)->调整图片的对比度   分为全局和局部的

"""
import cv2 as cv
import numpy as np


def equalHist_demo(image):  # 自动调整对比度 是图像增强的一个手段   (是全局的)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 先将其变成灰色
    dst = cv.equalizeHist(gray)
    cv.imshow("equal_demo", dst)


def clahe_demo(image):  # 局部的
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 先将其变成灰色
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # clipLimit是对比度的大小和限制  tileGridSize 格的大小
    dst = clahe.apply(gray)
    cv.imshow("clahe_demo", dst)


# 创建一个直方图
def create_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16*16*16, 1], np.float32)  # 16*16*16 之前那个公式算bins那个 1 表示 一维的  注意是float32的
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)  # 一定要转化为int类型的
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)  # 巴氏距离
    match2 = cv.compareHist(hist1, hist2 ,cv.HISTCMP_CORREL)  # 相关性
    match3 = cv.compareHist(hist1, hist2 ,cv.HISTCMP_CHISQR)  # 卡方
    print("巴氏距离: %s, 相关性: %s, 卡方: %s" % (match1, match2, match3))  # 这几个数值越大 越不相似


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
# clahe_demo(src)

image1 = cv.imread("D:/vcprojects/images/Crystal.jpg")
image2 = cv.imread("D:/vcprojects/images/CrystalLiu1.jpg")
cv.imshow("image1", image1)
cv.imshow("image2", image2)

hist_compare(image1, image2)

cv.waitKey(0)

cv.destroyAllWindows()
