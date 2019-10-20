import cv2 as cv
import numpy as np


def add_demo(m1, m2):
    dst = cv.add(m1, m2)  # dst是返回的结果
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)  # dst是返回的结果
    cv.imshow("subtract_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)  # dst是返回的结果
    cv.imshow("multiply_demo", dst)


def divide_demo(m1, m2):  # 相处的时候是就变成很少的数值了  所以就变得比较黑  所以用的相对少一些
    dst = cv.divide(m1, m2)  # dst是返回的结果
    cv.imshow("divide_demo", dst)


def logic_demo(m1, m2):
    # dst = cv.bitwise_and(m1, m2)  # 与运算 只有是1的时候才能变成1    黑色的是0 与其他的东西一与 还是变成 0 就i是漆黑一片
    # dst = cv.bitwise_or(m1, m2)  # 或运算 只有全是0的时候才是0 否则是1 所以说呢 白色的地方全是1 就变白咯
    image = cv.imread("D:/vcprojects/images/demo.png")
    cv.imshow("image1", image)
    dst = cv.bitwise_not(image)  # 取非的时候 速度杠杆的！！   也就是255-image  按位取反
    cv.imshow("logic_demo", dst)


def contrast_brightness_demo(image, c, b):
    h, w, c = image.shape
    blank = np.zeros([h, w, c], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)  # 图像混合，c, 1-c为这两张图片的权重
    cv.imshow("con-bri-demo", dst)


def others(m1, m2):  # 求出均值
    # M1 = cv.mean(m1)  # 第一个的值偏低 因为是偏暗的
    # M2 = cv.mean(m2)  # 这三个数分别是 R G B的形式的
    # cv.mean()
    # print(M1)
    # print(M2)
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)

    print(dev1)  # 方差越大 说明图像的差异越大
    print(dev2)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


print("-------Hello Python------")
src1 = cv.imread("D:/vcprojects/images/LinuxLogo.jpg")
src2 = cv.imread("D:/vcprojects/images/WindowsLogo.jpg")
print(src1.shape)   # 获取图像的长 宽 和通道
print(src2.shape)
cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)  # 黑色的地方是0 和任何数相加后不变 白色的地方是255 和任何数相加后 超过最大值 截断之后不变 所以还是白色
cv.imshow("image2", src2)

src = cv.imread("D:/vcprojects/images/demo.png")
cv.imshow("image2", src)
contrast_brightness_demo(src, 1.2, 10)  # 对比度是1.2 亮度增强了10个
# add_demo(src1, src2)
# subtract_demo(src1, src2)   # 相减的时候 255 减去其他的数字 就变成五颜六色的了
# divide_demo(src1, src2)
# others(src1, src2)  # 这个图片Linux周围是有反锯齿的 周围有平滑 有模糊所以有些像素并不为0  相乘后 由于一个值 相乘后就产生这种效果
# logic_demo(src1, src2)
cv.waitKey(0)

cv.destroyAllWindows()

