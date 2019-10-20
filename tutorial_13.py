"""

图像的二值化
二值图像 用0和1表示  很好压缩
图像二值化的方法
全部阈值
局部阈值

# 二值图像就是将灰度图转化成黑白图，没有灰，在一个值之前为黑，之后为白
# 有全局和局部两种
# 在使用全局阈值时，我们就是随便给了一个数来做阈值，那我们怎么知道我们选取的这个数的好坏呢？答案就是不停的尝试。
# 如果是一副双峰图像（简 单来说双峰图像是指图像直方图中存在两个峰）呢？
# 我们岂不是应该在两个峰之间的峰谷选一个值作为阈值？这就是 Otsu 二值化要做的。
# 简单来说就是对 一副双峰图像自动根据其直方图计算出一个阈值。
# （对于非双峰图像，这种方法 得到的结果可能会不理想）。



"""
import cv2 as cv
import numpy as np


# 全局阈值
def threshold_demo(image):
    # 这个函数的第一个参数就是原图像，原图像应该是灰度图。
    # 第二个参数就是用来对像素值进行分类的阈值。
    # 第三个参数就是当像素值高于（有时是小于）阈值时应该被赋予的新的像素值
    # 第四个参数来决定阈值方法，见threshold_simple()
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # cv.THRESH_OTSU 这个是自动寻找阈值的方法 有不同的方法
    # ret, binary = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)  # 可以设置0的位置的值 cv.THRESH_OTSU如果不指定的话  cv.THRESH_BINARY_INV 是相反的意思  这个100  表示大于100的表示白色 小于的表示黑色
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)  # 截断效果 大于127的时候是127的值 小于的时候不变
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)
    # 在前面的部分我们使用是全局阈值，整幅图像采用同一个数作为阈值。
    # 当时这种方法并不适应与所有情况，尤其是当同一幅图像上的不同部分的具有不同亮度时。
    # 这种情况下我们需要采用自适应阈值。此时的阈值是根据图像上的 每一个小区域计算与其对应的阈值。
    # 因此在同一幅图像上的不同区域采用的是不同的阈值，从而使我们能在亮度不同的情况下得到更好的结果。
    # 这种方法需要我们指定三个参数，返回值只有一个
    # _MEAN_C：阈值取自相邻区域的平均值,_GAUSSIAN_C：阈值取值相邻区域 的加权和，权重为一个高斯窗口。
    # Block Size - 邻域大小（用来计算阈值的区域大小）。
    # C - 这就是是一个常数，阈值就等于的平均值或者加权平均值减去这个常数。


# 局部阈值 轮廓更清晰
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)  # blocksize 25 必须是奇数
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)  # 高斯means的效果更好
    cv.imshow("binary", binary)


# 定制化的
def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])  # 变成一行多列的数组
    mean = m.sum() / (w*h)  # 求出整个灰度图像的平均值
    print("mean", mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow("binary", binary)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
custom_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()
