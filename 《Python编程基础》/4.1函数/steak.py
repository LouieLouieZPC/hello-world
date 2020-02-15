#!/usr/bin/env python3
# -*-coding:utf-8-*-
'a test module'  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__auther__='Frank Yeats'  # 使用__author__变量把作者写进去 

def make_steak(d,*other):
    '''做一份牛排'''
    print('Make a steak well done in %d'%d+' with the other:')
    for i in other:
        print('———'+i)
