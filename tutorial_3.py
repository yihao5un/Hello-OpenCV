"""
色彩空间 对角线表示
常见的色彩空间 RGB HSV HIS YCrCb YUV
最常见的色彩转换就是HSV与RGB YUV与RGB  HSV=RGB的转换真的很重要 H:0-180 S:0-255 V:0-255
"""
import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("D:/vcprojects/images/video_006.mp4")
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])  # HSV中绿色的最低值
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)  # 参数分别需要指定HSV的绿色的高值和低值
        dst = cv.bitwise_and(frame, frame, mask=mask)
        cv.imshow("video", frame)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:  # 27 是esc
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb", Ycrcb)
    hls = cv.cvtColor(image, cv.COLOR_BGR2HLS)
    cv.imshow("hls", hls)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input images", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

b, g, r = cv.split(src)  # 通道分离
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)


src = cv.merge([b, g, r])  # 又和之前的图片一模一样咯   注意应该输入一个数组
src[:, :, 2] = 0  # 对某一个通道赋值 最后一个通道赋值为0 就是把红色给弄没 那个2的意思也就是bgr中的r 给赋值为0也就是给弄没
cv.imshow("changed image", src)
extrace_object_demo()
cv.waitKey(0)

cv.destroyAllWindows()
