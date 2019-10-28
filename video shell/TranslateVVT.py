from langconv import *
import sys
import os


# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line


base_dir = "C:\\Users\\LHYF\\Desktop\\youtube\\vvt"
files = os.listdir(base_dir)
i = 0
for file in files:
    arr = str(file).split(".")
    if arr[-1] == "vtt":
        i = i + 1
        print(str(i) + str(arr[0]))
        source = open(str(base_dir +"/" + file),"r", encoding='utf-8')
        target = open(str(base_dir +"\\target\\" + arr[0]+"-simple.vvt"),"w", encoding='utf-8')
        content = source.readline()
        while len(content) > 0:
            content = cht_to_chs(content)
            print(content)
            target.writelines(content)
            content = source.readline()

        target.close()
        source.close()











