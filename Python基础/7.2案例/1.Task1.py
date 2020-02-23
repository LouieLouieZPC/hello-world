#!/user/bin/env python3
# -*-coding:utf-8-*-
'''
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对路径和相对路径。
'''

import os

cha_file=input("输入查找的字符串：\n")
'''
os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
str.find(str, beg=0, end=len(string))

Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。str.replace(old, new[, max])

'''

for dir in os.walk(os.path.abspath('.')):  # 输出（在当前目录的绝对路径中的）文件名，向上或者向下
    for x in dir[-1]:
    # 文件目录
        if x.find(cha_file)!=-1:    # 包含子字符串
            y=os.path.join(dir[0],x)
        # 获得文件的绝对路径y
            print('绝对路径为:',y)
            k=y.replace(os.path.abspath('.'),'')
            print('相对路径为:',k)