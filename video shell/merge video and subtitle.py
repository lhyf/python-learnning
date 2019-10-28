# coding:utf-8
import os

'''
使用ffmpeg 合并视频与音频文件
'''

files = os.listdir()
for file in files:
    file_name = str(file)
    arr = file_name.split(".")
    ext = arr[-1]  # 获取文件扩展名
    name = file_name[0:-(len(ext)+1)] #获取文件名
    if ext == "mp4":
        #   ffmpeg -i "The Most Efficient Way to Destroy the Universe.mp4" -vf subtitles="The Most Efficient Way to Destroy the Universe.vtt" output2.mp4
        # print('ffmpeg -i "' + arr[0] + '.mp4" -vf subtitles="' + arr[0] + '.-simple.vtt" "' + arr[0] + ' subtitle.mp4"')
        os.system(r'ffmpeg -i "' + name + '.mp4" -vf subtitles="' + name + '.srt" "' + name + '-subtitle.mp4"')

        print(name + ".mp4 已完成")






