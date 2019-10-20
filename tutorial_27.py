"""
案例实战-数字验证码的识别
    OpenCV+Tesserct-OCR
    OpenCV预处理
    Tesserct-OCR验证码识别

知识点
    预处理
    不同的结构元素中选择
    Image与numpy array相互转化
    识别与输出
"""


import cv2 as cv
import numpy as np
import pytesseract
from PIL import Image
import pytesseract as tess


def recogize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)  # 加上INV后就变成黑色底白色字了呢
    # 去除干扰线
    kernal = cv.getStructuringElement(cv.MORPH_RECT, (4, 4))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kernal)  # 结构元素输出的结果
    cv.imshow("binary-image", bin1)

    cv.bitwise_not(bin1, bin1)
    textImage = Image.fromarray(bin1)
    text = tess.image_to_string(textImage)
    print("识别结果：%s" % text)




print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/yzm.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
recogize_text()
cv.waitKey(0)
cv.destroyAllWindows()
