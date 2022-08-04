#coding:utf-8#
# ---- 视频转图片序列 ---- #
import os
import cv2
import numpy as np
from natsort import natsorted

# ---- 路径设置 ---- #
in_vid_dir = 'C:/Users/syyyyyw/Desktop/xxxxxxx.mp4'
out_vid_dir = 'C:/Users/syyyyyw/Desktop/xxxxxx'  # 不能用r和\会报错。  路径不对会按照最后字符命名

# ---- 加载视频 ---- #
print(in_vid_dir)
cap = cv2.VideoCapture(in_vid_dir)  # 打开相机
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 获取视频帧率
totalFrame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 总帧数
print('All-Frames:', totalFrame)

# ---- 循环加载 ---- #
count = 1
while True:
    ret, frame = cap.read()  # 捕获一帧图像
    if ret:
        print(str(count) + ':' + str(totalFrame))
        if count % 5 == 0:
            cv2.imwrite(out_vid_dir +"/"+ str(int(count / 5)) + '.jpg', frame)
        cv2.waitKey(1)
        count = count + 1
    else:
        break
cap.release()
