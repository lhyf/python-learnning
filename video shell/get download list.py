# coding:utf-8
import os
'''
打印指定目录中的MP4,并打印其视频id(youtube)
'''
files = os.listdir("C:\\Users\\LHYF\\Desktop\\youtube\\download")
for file in files:
    arr = str(file).split(".")
    if arr.__len__() > 0 and arr[1] == "mp4":
        print("youtube " + arr[0][-11:])

# files = os.listdir()
# for file in files:
#     print(str(file))
#     arr = str(file).split(".")
#     if arr.__len__() > 0 and arr[1] == "mp4":
#         print(str(arr[0]))
#         print(arr[0][-11:])
