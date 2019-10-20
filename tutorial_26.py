"""
人脸检测   嘤嘤嘤~~~
    HAAR 与 LBP 数据
    相关API使用

HAAR github上的项目

"""


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # face_detector = cv.CascadeClassifier("F:/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")  # 通过级联检测器 检测 这个是 基于 HAAR 的检测  那个 1.02是帧率呢
    face_detector = cv.CascadeClassifier("F:/opencv-master/data/lbpcascades/lbpcascade_frontalcatface.xml")  # 基于LBP的呢
    faces = face_detector.detectMultiScale(gray, 1.02, 5)  # 这个5是识别的级别 如果是很高的话 就需要有很清晰的脸 对脸的要求比较高   是一个一个的矩形框
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("result", image)


import cv2 as cv
import numpy as np


print("-------Hello Python------")
# src = cv.imread("D:/vcprojects/images/CrystalLiu1.jpg")  # 对于图像来说


# 对于视频来说
capture = cv.VideoCapture(0)
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.namedWindow("result", cv.WINDOW_AUTOSIZE)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)  # 那个1是为了解决镜像问题
    face_detect_demo(frame)

    c = cv.waitKey(10)
    if c == 27:  # ESC
        break

# cv.imshow("input image", src)
cv.waitKey(0)
cv.destroyAllWindows()
