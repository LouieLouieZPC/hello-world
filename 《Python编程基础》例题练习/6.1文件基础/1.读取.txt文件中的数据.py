# 打开
# 读取


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
with open(r'e_point.txt','r') as if:
    print(if.read())