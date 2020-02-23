#!/user/bin/env python3
# -*-coding:utf-8-*-
'''
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

import os

cha_file=input("输入查找的字符串：\n")

# walk()函数用于通过在目录树中游走输出在目录中的文件名 向上或向

for dir in os.walk(os.path.abspath('.')):
    for x in dir[-1]:
    # 文件目录
        if x.find(cha_file)!=-1:
            y=os.path.join(dir[0],x)
        # 获得文件的绝对路径y
            print('绝对路径为:',y)
            k=y.replace(os.path.abspath('.'),'')
            print('相对路径为:',k)