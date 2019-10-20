"""

！！！Canny边缘提取
Canny 在1986年提出
是一个很好的边缘检测器
很常用也很实用的图像处理方法
总共有五步
1.高斯模糊-GaussianBlur
2.灰度转换-cvtColor
3.计算梯度-Sobel/Scharr
4.非最大信号抑制

# 算法使用一个3×3邻域作用在幅值阵列M[i,j]的所有点上；
# 每一个点上，邻域的中心像素M[i,j]与沿着梯度线的两个元素进行比较，
# 其中梯度线是由邻域的中心点处的扇区值ζ[i,j]给出。
# 如果在邻域中心点处的幅值M[i,j]不比梯度线方向上的两个相邻点幅值大，则M[i,j]赋值为零，否则维持原值；
# 此过程可以把M[i,j]宽屋脊带细化成只有一个像素点宽，即保留屋脊的高度值。


边缘的信号很强，但边缘只能有一个，
不能说你这么很宽都是边缘，所以要对非边缘的一些像素进行压制
就是如果在它的方向上面如果它不是最大值的话我们就把它去掉，切向是角度的方向，法向是它跟垂直90度的方向，
在它左右两边如果值都小于当前的这个那么我们就把它去掉
对图像所有的点都做非最大信号抑制


5.高低阈值输出二值图像

T1, T2为阈值 凡是高于T2都保留 凡是小于T1的都丢弃 从高于T2的像素出发 凡是大于T1 而且相互连接的 都保留
最终得到一个输出二值图像
推荐的高低阈值比值为 T2 ：T1 = 3：1 / 2：1 其中T2为高阈值 T1为低阈值



"""

import cv2 as cv
import numpy as np


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)  # blur可以降低噪声
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # x gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)  # 注意不能是浮点数 应该是CV_16SC1
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    # 求边缘
    # edge_output = cv.Canny(xgrad, ygrad, 50, 150)  # 低阈值是50 高阈值150 是3倍的
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    # 输出为彩色边缘
    dst = cv.bitwise_and(image, image, mask=edge_output)  # 按位与
    cv.imshow("Color Edge", dst)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
edge_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()
