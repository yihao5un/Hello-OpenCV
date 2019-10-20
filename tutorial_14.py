import cv2 as cv
import numpy as np


# 将大图片拆分成小图片后再用自适应局部阈值比较好
def big_image_binary(image):
    print(image.shape)
    cw = 256  # 小图片的宽高
    ch = 256
    h, w = image.shape[:2]  # 取出图像的宽高
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):  # 这个ch是步长
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:cw+col]  # ROI是Region of Interest的简写，指的是在“特征图上的框”
            # ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 必须有ret 返回值的        全局的方法有噪声
            # 局部的方法 比较好
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)  # 20 相当于噪声
            gray[row:row + ch, col:cw + col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("D:/vcprojects/images/result_binary.png", gray)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/big_image.jpg")
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
# cv.imshow("input image", src)
big_image_binary(src)
cv.waitKey(0)

cv.destroyAllWindows()
