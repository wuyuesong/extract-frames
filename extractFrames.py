#python程序接收两个参数，实现对视频文件每隔几秒抽帧，保存成图片，第一个参数为视频文件位置，第二个参数为间隔秒数
import cv2
import sys
import os
import math
import argparse

# 定义函数extract_frames，接收两个参数：视频文件路径video_path和间隔秒数interval
def extract_frames(video_path, interval):
    # 判断video_path是文件还是文件夹
    if os.path.isfile(video_path):
        # 使用cv2.VideoCapture()函数读取视频文件
        cap = cv2.VideoCapture(video_path)
        # 定义计数器count，初始值为0
        count = 0
        # 当视频文件打开时，执行循环
        while cap.isOpened():
            # 使用cap.read()函数读取视频文件的每一帧
            ret, frame = cap.read()
            # 如果读取到的帧为空，则退出循环
            if not ret:
                break
            # 计数器count加1
            count += 1
            # 如果计数器count是间隔秒数interval乘以视频文件的帧率的倍数，则保存当前帧为一张图片
            if count % (interval * math.ceil(cap.get(cv2.CAP_PROP_FPS))) == 0:
                # 创建data目录
                if not os.path.exists('data'):
                    os.makedirs('data')
                # 保存图片到data目录下
                cv2.imwrite(f"data/frame{count}.jpg", frame)
                print(f"data/frame{count}.jpg")
        # 释放视频文件
        cap.release()
    elif os.path.isdir(video_path):
        # 遍历文件夹下的所有视频文件
        for filename in os.listdir(video_path):
            if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mov'):
                # 使用cv2.VideoCapture()函数读取视频文件
                cap = cv2.VideoCapture(os.path.join(video_path, filename))
                # 定义计数器count，初始值为0
                count = 0
                # 当视频文件打开时，执行循环
                while cap.isOpened():
                    # 使用cap.read()函数读取视频文件的每一帧
                    ret, frame = cap.read()
                    # 如果读取到的帧为空，则退出循环
                    if not ret:
                        break
                    # 计数器count加1
                    count += 1
                    # 如果计数器count是间隔秒数interval乘以视频文件的帧率的倍数，则保存当前帧为一张图片
                    if count % (interval * math.ceil(cap.get(cv2.CAP_PROP_FPS))) == 0:
                        # 创建data目录
                        if not os.path.exists('data'):
                            os.makedirs('data')
                        # 保存图片到data目录下
                        cv2.imwrite(f"data/{filename}_frame{count}.jpg", frame)
                        print(f"data/{filename}_frame{count}.jpg")
                # 释放视频文件
                cap.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='从视频文件中提取帧并保存为图片')
    parser.add_argument('video_path', type=str, help='视频文件路径')
    parser.add_argument('interval', type=int, help='保存帧的间隔秒数')
    args = parser.parse_args()

    # 调用函数extract_frames，传入视频文件路径和间隔秒数
    extract_frames(args.video_path, args.interval)