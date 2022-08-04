import cv2
import sys

input_path = 'C:/Users/syyyyyw/Desktop/2R9A9700.MOV'
output_path = 'C:/Users/syyyyyw/Desktop/'



def select_video(input_path, output_path, start=500, end=-1):
    """
    input_path表示原视频路径
    output_path表示要保存路径
    start表示起始的帧,默认从头开始
    end表示终止帧，默认到结尾
    """
    assert start < end, "起始帧位置要小于终止帧位置"
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    # print()
    #     fps = int(cap.get(cv2.CAP_PROP_FPS)) #有些文件该值无法获取
    fps = 25
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)
    print('fps', fps)
    print('size', size)

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 该值有时也读不出来要注意
    if num_frames < 0:
        num_frames = end

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # *'XVID' 保存AVI视频
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), True)
    i = 1
    j = 0
    end = min(end, num_frames)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting...")
            break
        if i >= start and i <= end:
            out.write(frame)
            j = j + 1
        i = i + 1
        sys.stdout.write('\r%d/%d finished!' % (j, end - start + 1))
        sys.stdout.flush()

    cap.release()
    out.release()
