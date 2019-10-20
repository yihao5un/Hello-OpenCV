"""

边缘保留滤波(EPF) 也就是美颜效果

高斯双边
均值迁移
操作

"""
import cv2 as cv
import numpy as np


"""
    同时考虑空间与信息和灰度相似性，达到保边去噪的目的
    双边滤波的核函数是空间域核与像素范围域核的综合结果：
    在图像的平坦区域，像素值变化很小，对应的像素范围域权重接近于1，此时空间域权重起主要作用，相当于进行高斯模糊；
    在图像的边缘区域，像素值变化很大，像素范围域权重变大，从而保持了边缘的信息。
 """


def bi_demo(image):  # 高斯双边模糊 很好的美颜工具23333333333
    dst = cv.bilateralFilter(image, 0, 100, 15)  # 高斯双边 一般把d设置为0 从sigmaColor 和 sigmaSpace 反算出d
    cv.imshow("bi_demo", dst)

# InputArray src: 输入图像，可以是Mat类型，图像必须是8位或浮点型单通道、三通道的图像。 
# OutputArray dst: 输出图像，和原图像有相同的尺寸和类型。 
# int d: 表示在过滤过程中每个像素邻域的直径范围。如果这个值是非正数，则函数会从第五个参数sigmaSpace计算该值。 
# double sigmaColor: 颜色空间过滤器的sigma值，这个参数的值月大，表明该像素邻域内有越宽广的颜色会被混合到一起，产生较大的半相等颜色区域。 （这个参数可以理解为值域核的）
# double sigmaSpace: 坐标空间中滤波器的sigma值，如果该值较大，则意味着越远的像素将相互影响，从而使更大的区域中足够相似的颜色获取相同的颜色。当d>0时，d指定了邻域大小且与sigmaSpace无关，否则d正比于sigmaSpace. （这个参数可以理解为空间域核的）
# int borderType=BORDER_DEFAULT: 用于推断图像外部像素的某种边界模式，有默认值BORDER_DEFAULT


def shift_demo(image):  # 均值迁移 如果差值很小的话 就漂移 模糊起来 可能造成过度模糊 类似于油画的效果
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)  # 彩色图像分割
    cv.imshow("shift_demo", dst)

# 这两个都是EPF


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
