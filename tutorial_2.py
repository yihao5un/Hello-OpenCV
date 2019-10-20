import cv2 as cv
import numpy as np


def access_pixels(image):  # pixels是像素的意思 读取属性    时间很长 因为解释性的语言 一步一步执行
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height : %s, channels : %s " % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo", image)


def inverse(image):  # 取反之后 速度很快 调用的是c的代码
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)


def create_image():

    """ 多通道
    img = np.zeros([400, 400, 3], np.uint8)  # np.uint8表示赋值的位置
    # img[:, :, 0] = np.ones([400, 400])*255   # B  G  R  是从0 开始的 所以第一个是0 表示 blue
    img[:, :, 2] = np.ones([400, 400]) * 255
    cv.imshow("new image", img)

    """

    """单通道
    
    img = np.zeros([400, 400, 1], np.uint8)     # zeros->Return a new array of given shape and type, filled with zeros.
                                                # uint8应该是无符号8位二进制整型, 其实就是unsignedchar类型
    img[:, :, 0] = np.ones([400, 400])*127  # 127 就是灰度的  单通道的一般的灰度图像   多通道的一般是RGB图像 np.ones 是变成1 可以乘法
    cv.imshow("new image", img)
    cv.imwrite("D:/myImages.png", img)
    """

    m1 = np.ones([3, 3], np.uint8)  # 最好选择浮点型float 避免被截断
    m1.fill(122222.388)
    print(m1)

    m2 = m1.reshape([1, 9])  # 变成一行9列  之前是三行三列 reshape 用于改变维数
    print(m2)

    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.int32)  # int32 类型什么的一定要掌握
    # m3.fill(9)  # 如果是fill(9)的话 就自动向里面填入数字9
    print(m3)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")  # blue, green, red
cv.namedWindow("input images", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()  # 读取图片之前
create_image()
t2 = cv.getTickCount()  # 读取图片之后
time = (t2-t1)/cv.getTickFrequency()
print("time : %s ms " % (time*1000))  # getTIckFrequency() 是获取秒数 *1000 就是毫秒数
cv.waitKey(0)

cv.destroyAllWindows()
