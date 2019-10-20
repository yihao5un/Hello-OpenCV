"""

模板匹配 模板是想要检测的地方 从左到右 从上到下
匹配算法介绍

# 模板匹配，就是在整个图像区域发现与给定子图像匹配的小块区域，
# 需要模板图像T和待检测图像-源图像S
# 工作方法：在待检测的图像上，从左到右，从上倒下计算模板图像与重叠子图像匹配度，
# 匹配度越大，两者相同的可能性越大。

"""
import cv2 as cv
import numpy as np


def template_demo():
    tpl = cv.imread("D:/vcprojects/images/tpl.png")  # 模板图片
    target = cv.imread("D:/vcprojects/images/test1.png")  # 目标图片
    cv.imshow("template_image", tpl)
    cv.imshow("target_image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]  # normed 是赋范  是否要进行归一化
    th, tw = tpl.shape[:2]  # 取出高度和宽度
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc  # tl是topleft 就是矩形左上角的点
        else:
            tl = max_loc

        br = (tl[0]+tw, tl[1]+th)

        cv.rectangle(target, tl, br, (0, 0, 255), 2)
        cv.imshow("match-"+np.str(md), target)
        # cv.imshow("match-" + np.str(md), result)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
template_demo()
cv.waitKey(0)

cv.destroyAllWindows()
