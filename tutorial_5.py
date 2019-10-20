import cv2 as cv
import numpy as np

"""
ROI（region of interest），感兴趣区域。机器视觉、图像处理中，
从被处理的图像以方框、圆、椭圆、不规则多边形等方式勾勒出需要处理的区域，
称为感兴趣区域，ROI。在Halcon、OpenCV、Matlab等机器视觉软件上常用到各种算子（Operator）和函数来求得感兴趣区域ROI，
并进行图像的下一步处理。

ROI 用numpy获取 长宽高等

"""

"""
泛红填充操作，如何填充一个对象内部的区域
-FLOODFILL_FIXED_RANGE - 改变图像，泛洪填充
-FLOODFILL_MASK_ONLY - 不改变图像，只填充遮罩层本身，忽略新的颜色值参数

floodFill(Mat image, Mat mask, Point seedPoint, Scalar newVal)

floodFill(image, mask, seedPoint, newVal, rect, loDiff, upDiff, flags)

src(seed.x,seed.y)-loDiff <= src(x,y) <= src(seed.x,seed.y)+upDiff

"""

"""
模糊操作基本原理
1.基于离散卷积
2.定义好每个卷积核
3.不同卷积核得到不同的卷积效果
4.模糊是卷积的一种表象


卷积原理
一维卷积...卷积边缘...


"""


def fill_color_demo(image):  # 泛红填充彩色图像
    copyImg = image.copy()
    h, w = image.shape[:2]  # 获取前两个 宽和高的值   注意要加上shape
    mask = np.zeros([h+2, w+2], np.uint8)  # mask 的初始值 必须是+2
    # 参数：原图，mask图，起始点，起始点值减去该值作为最低值，起始点值加上该值作为最高值，彩色图模式
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyImg)


def fill_binary():
    image = np.zeros([400, 400, 3], np.uint8)  # 创建一个图片 大小是400*400  每个像素点 各站一个通道 24位图像
    image[100:300, 100:300, :] = 255  # 给各个通道赋值255
    cv.imshow("fill_binary", image)

    mask = np.ones([402, 402, 1], np.uint8)  # 初始化 mask一定是+2 而且是单通道
    mask[101:301, 101:301] = 0  # 造一个mask 像填充的位置要初始化为0 使用floodfill的时候 只有不为1的地方才能被填上
    # 200,200表示填充的区域 0，0，255 BGR 表示红色 而且只填充 mask部分
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary", image)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

# fill_color_demo(src)
fill_binary()

"""

face = src[50:250, 100:300]  # 显示长和宽的范围  也就是说 剪切的区域
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)  # 变成灰色的
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)  # 变成原色
src[50:250, 100:300] = backface  # 把灰色这块又重新填到原图里面去了
cv.imshow("face", src)

"""
cv.waitKey(0)

cv.destroyAllWindows()
