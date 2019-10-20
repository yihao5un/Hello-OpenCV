"""

其他的形态学操作
    顶帽
    黑帽
    形态学梯度

顶帽 tophat
    是原图像与开操作之间的额差值图像

黑帽 blackhat
    是闭操作图像与源图像的差值图像

形态学梯度-Gradient
    基本梯度
        基本梯度是用膨胀后的图像减去腐蚀后的图像得到的差值图像 称为梯度图像也是opencv中支持的计算形态学梯度的方法并称为基本梯度
    内部梯度
        使用原图像减去腐蚀后的图像得到的差值图像
    外部梯度
        使用膨胀后的图像减去原来的图像得到的差值图像

"""




import cv2 as cv
import numpy as np


def hat_gray_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 获取结构元素
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)  # 形态学操作   cv.MORPH_TOPHAT  是顶帽操作  换成cv.MORPH_BLACKHAT是黑帽的操作

    # 提升下亮度
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    cv.add(dst, cimage)

    cv.imshow("tophat", dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255 , cv.THRESH_BINARY | cv.THRESH_OTSU)  # 变成二值图像
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  # 获取结构元素
    dst = cv.morphologyEx(binary, cv.MORPH_TOPHAT, kernel)  # 形态学操作   cv.MORPH_TOPHAT  是顶帽操作  换成cv.MORPH_BLACKHAT是黑帽的操作

    # # 提升下亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # cv.add(dst, cimage)

    cv.imshow("tophat", dst)



def gradient_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255 , cv.THRESH_BINARY | cv.THRESH_OTSU)  # 变成二值图像
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 获取结构元素
    dst = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)  # 形态学操作   cv.MORPH_TOPHAT  是顶帽操作  换成cv.MORPH_BLACKHAT是黑帽的操作  cv.MORPH_GRADIENT 是梯度

    # # 提升下亮度
    # cimage = np.array(gray.shape, np.uint8)
    # cimage = 100
    # cv.add(dst, cimage)

    cv.imshow("tophat", dst)


def gradient2_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))  # 获取结构元素
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # internal gradient
    dst2 = cv.subtract(dm, image)  # external gradient
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# hat_gray_demo(src)
# hat_binary_demo(src)
# gradient_binary_demo(src)
gradient2_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
