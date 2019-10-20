import cv2 as cv
import numpy as np


# 均值模糊
def blur_demo(image):  # 对于随机噪声有一个很好的去噪效果
    dst = cv.blur(image, (5, 5))  # (5, 5)是卷积核的大小 也就是几行几列x方向和y方向  通俗来说就是模糊的方向 数值越大那么模糊的越厉害
    cv.imshow("blur_demo", dst)  # 时间复杂度是O（n）


# 中值模糊
def medium_blur_demo(image):
    dst = cv.medianBlur(image, 5)  # 去除椒盐噪声点  有一个很好的去噪效果
    cv.imshow("medium_blur_demo", dst)


# 自定义模糊
def custom_blur_demo(image):
    # kernel = np.ones([5, 5], np.float32)/25  # 初始化定义一个5*5的全是1的 除以25是防止溢出
    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9  # 用一个3*3数组的 每个位置都是1的
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) / 9  # 锐化算子 变得更有立体感
    # filter2D(src, ddepth(图像深度，-1表示默认和src一样深度), kernel, dst=None, anchor=None(锚点，卷积核中心), delta=None, borderType=None)
    dst = cv.filter2D(image, -1, kernel=kernel)  # int ddepth: 目标图像深度，如果没写将生成与原图像深度相同的图像。
    cv.imshow("custom_blur_demo", dst)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# blur_demo(src)
# medium_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)


cv.destroyAllWindows()


"""

高斯模糊
“中间点”取”周围点”的平均值，就会变成1。在数值上，这是一种”平滑化”。在图形上，就相当于产生”模糊”效果，”中间点”失去细节。
如果使用简单平均，显然不是很合理，因为图像都是连续的，越靠近的点关系越密切，越远离的点关系越疏远。因此，加权平均更合理，距离越近的点权重越大，距离越远的点权重越小。
正态分布显然是一种可取的权重分配模式。
计算平均值的时候，我们只需要将”中心点”作为原点，其他点按照其在正态曲线上的位置，分配权重，就可以得到一个加权平均值。

"""