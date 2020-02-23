
*********************************StringIO**************************************

'''
一、
StringIO顾名思义就是在内存中读写str（字符串）
要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
f.write()写入
f.getvalue()

如下：
'''
from io import StringIO   # 导入io库中的StringIO类
f=StringIO()              # 创建类的实例
print(f.write('Hello'))   # 写入
print(f.write(' '))
print(f.write('World!'))
print(f.write('----烨辞'))
print(f.getvalue())       # getvalue()方法用于获得写入后的str

# Output:
5
1
6
6
Hello World!----烨辞



-----------------------------------------------------------------------------------


'''
二、
要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
'''

from io import StringIO
f=StringIO('Hello!\nHi!\nGoodbye!')  # 一个str初始化StringIO
while True:
    r=f.readline()    # 按行读取
    if r=='':
        break
    print(r.strip())  # 去除换行符

# Output:
Hello!
Hi!
Goodbye!



*********************************BytesIO**************************************
'''
BytesIO顾名思义就是在内存中读写bytes（字节）
我们创建一个BytesIO，然后写入一些bytes：
'''

from io import BytesIO
f=BytesIO()
print(f.write('中文'.encode('utf-8')))  # 写入的不是str，而是经过encode函数的UTF-8编码的bytes
print(f.getvalue())    #  getvalue()方法用于获得写入后的str

# Output:
6
b'\xe4\xb8\xad\xe6\x96\x87'



-----------------------------------------------------------------------------------


'''
和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
'''

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'





