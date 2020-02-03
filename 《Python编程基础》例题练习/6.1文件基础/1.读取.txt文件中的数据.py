'''
1.打开,路径记得加r声明字符串不用转义 with open(r'','r/w/a/r+') as f:
try...finally...
f.close()
2.读取:
x=f.read()字符串
x=f.readline()字符串
x=f.readlines()列表


'''

# 7.3打开并读取文件
f=open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r')     # 只读文件，读取模式通过绝对路径打开文件并定义变量f
txt=f.read()   # 用read读取整个文件内容并赋值给变量txt
print(txt)     # 打印文件内容
'''
以上结果如下：
2.7182818284
4904523536
0287471352
'''


# 7.4关闭文件
f.close()



# 7.5用try..finally...结构确保正常关闭文件
try:
    f=open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r')
    print(f.close())
finally:
    if f:
        f.close()



# 7.6使用with语句，与用try..finally...结构效果一样
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:  # 打开
    print(f.read())    # 读取








# 7.7相对文件路径
with open(r'《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:      # 打开
    print(f.read())   # 读取
'''
以上结果如下：
2.7182818284
4904523536
0287471352
'''
# 7.8绝对文件路径
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:
    print(f.read())
'''
以上结果如下：
2.7182818284
4904523536
0287471352
'''




#7.9 双反斜杠方式
with open('D:\\01.Software\\GitHub\\GitHub Repository\\hello-world\\《Python编程基础》例题练习\\6.1文件基础\\e_point.txt','r') as f:
    print(f.read())         # 结果同上

#7.10正斜杠方式
with open('D:/01.Software/GitHub/GitHub Repository/hello-world/《Python编程基础》例题练习/6.1文件基础/e_point.txt','r') as f:
    print(f.read())         # 结果同上





# 7.11 for循环来一一读取
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt'   # 将路径名称赋值给变量，以方便修改文件名称和路径
with open(file_name,'r') as f:
    for i in f:
        print(i)
'''
以上结果如下：
2.7182818284
                     # 空白行的出现是因为原文档每行末尾都有一个看不见的换行符
4904523536

0287471352
'''

# 7.12可以用retrip函数删除string字符串末尾的指定字符（默认为空格），lstrip函数（删除字符前面的指定字符）和strip函数（删除字符传首尾两端的指定字符串）
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt'   
with open(file_name,'r') as f:
    for i in f:                    # 迭代
        print(i.rstrip())          # retrip函数删除string字符串末尾的指定字符
'''
以上结果如下：
2.7182818284
4904523536
0287471352
'''

# 7.13read函数，读取，读取的内容存储道一个字符串变量中
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:  # 打开
    txts=f.read()      # 读取，读取的内容存储道一个字符串变量中
print(type(txts))      # 查看类型
print(txts)            # 输出
'''
以上结果如下：
>>> print(type(txts))
<class 'str'>
>>> print(txts)
2.7182818284
4904523536
0287471352
'''

# 7.14readlines函数，读取，将读取的一个文件存储到一个列表里
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:  # 打开
    txts=f.readlines()      # 读取，将读取的一个文件存储到一个列表里
print(type(txts))      # 查看类型
print(txts)            # 输出
'''
以上结果如下：
>>> print(type(txts))      # 查看类型
<class 'list'>
>>> print(txts)            # 单纯输出
['2.7182818284\n', '4904523536\n', '0287471352']
'''


# 7.15 打印readlines函数存储的数据
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:  # 打开
    txts=f.readlines()      # 读取，将读取的一个文件存储到一个列表里
for i in txts:
    print(i.strip())

'''
以上结果如下：        # 迭代，而非一次性输出
2.7182818284
4904523536
0287471352
'''


# readline函数，每次读取文件一行，将读取的一行内容存储到一个字符串变量里
with open(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\e_point.txt','r') as f:    # 打开
    txt=f.readline()      # readline函数，读取一行
print(type(txt))
print(txt)
'''
以上结果如下：
>>> print(type(txt))
<class 'str'>
>>> print(txt)
2.7182818284
'''