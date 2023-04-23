# extract-frames
由cursor生成

视频抽帧程序，间隔一段时间抽帧一次

**用法**

~~~shell
python extractFrames.py video_path interval
~~~

video_path 为视频路径，如果为视频文件则对该文件抽帧，如果是文件夹则对文件夹下的所有视频文件抽帧

interval 为间隔秒数

抽帧图片生成在data目录下，如果没有则创建
