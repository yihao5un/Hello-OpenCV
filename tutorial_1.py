import cv2 as cv
import numpy as np  # np作为科学计数的包 科技计算n维数组的对象


def video_demo():
    capture = cv.VideoCapture(0)  # 0 是摄像头的编号 或者 可以指定路径播放视频 opencv 读出来的视频是没有声音的
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)  # flip 是镜像调换 1 和 -1
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)  # 获取像素数据
    print(pixel_data)


print("-------Hello Python------")
src = cv.imread("D:/vcprojects/images/demo.png")
cv.namedWindow("input images", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
# get_image_info(src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 获取灰度图像
cv.imwrite("D:/result.png", gray)   # 保存图片
cv.waitKey(0)

cv.destroyAllWindows()
