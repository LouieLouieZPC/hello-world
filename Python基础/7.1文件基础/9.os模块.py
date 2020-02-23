'''
os.name                 # 获取当前操作系统
os.environ              # 查看操作系统中定义的环境变量
os.environ.get('key')   # 获取某个环境变量的值
os.sep                  # 查询文件路径的分隔符
os.linesep              # 查询当前系统使用的行终止符
os.getcwd()             # 查询当前工作路径
os.listdir()            # 查询当前目录下的文件

os.remove()             # 删除文件
os.mkdir()              # 创建文件夹（该文件夹事先不存在）
os.rmdir()              # 删除文件夹（该文件夹为空）

'''



# 查询操作系统
>>> import os       # 导入模块
>>> os.name         # 获取当前操作系统
'nt'
>>> os.sep          # 查询文件路径的分隔符
'\\'
>>> os.linesep      # 查询当前系统使用的行终止符
'\r\n'

# 查询工作路径
>>> path=os.getcwd()            # 查询当前工作路径
>>> print(path)
D:\01.Software\Python


# 查询指定路径下的文件
import os 
os.listdir(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础')   # 查询当前目录下的文件
'''
以下为结果：
['1.读取.txt文件中的数据.py', '2.Task1（打开并读取文件）.py', '3.写入和添加word.txt文件.py', '4.读取csv数据法一.py', '5.读取csv数据法二 .py', '6.将列表数据写入.csv文件.py', '7.将字典数据写
入.csv文件.py', '8.Task2（将列表以列的形式写入aquars.csv文件）.py', '9.os模块.py', 'e_point.txt', 'iris.csv', 'squares.py', 'text.csv', 'Walden.txt', 'word.txt']
'''


# 删除文件
import os
os.remove(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\text.csv')  # 删除文件

# 创建与删除目录
import os
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test'
os.mkdir(file_name)           # 创建文件夹
os.rmdir(file_name)           # 删除文件夹

# 7.35 os的功能实现
import os
system=os.name
if system=='nt':
    print('当前的操作系统是Windows.')
else:
    print('当前的操作系统是Linux.')
print('本系统表示路径的分隔符是：',[os.sep])
print('本系统中使用的行终止符为：',[os.linesep])

path=os.getcwd()          # 获得当前目录
print('运行本程序所在目录的是：',path)

print('计算机的path环境变量如下所示：\n',os.getenv('path'))

os.mkdir('test')                                     # 创建空文件夹
print('当前文件夹中的文件有：\n',os.listdir(path))     # 获取文件夹中的所有文件
if(os.path.exists('test')):                          # 判断文件是否存在
    os.rmdir('test')                                 # 删除指定文件
    print('删除文件夹')
else:
    print('文件夹不存在')
print('删除后的文件夹中的文件有：\n',os.listdir(path))

filepath1='python7'
if (os.path.isfile(filepath1)):                        # 判断是不是文件
    print(filepath1,'是一个文件')
else:
    print(filepath1,'不是一个文件')


******************************************************************************


name='README.md'
print('本程序的大小为：',os.path.getsize(name))
name=os.path.abspath(name)                             # 获取文件的绝对路径
print('本程序的绝对路径为：',name)
print('本程序的路径和文件名分别为：',os.path.split(name)) # 将文件名和路径分开
files=os.path.splitext(name)                           # 将文件名与扩展名分开
print('本程序的扩展名为：',files[1])
print('本程序的文件名为：',os.path.basename(name))       # 获取文件的名字
print('本程序的路径为：',os.path.dirname(name))          # 获取文件的路径

例如：

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')   # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

>>> os.path.split('/Users/michael/testdir/file.txt')  # 要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
('/Users/michael/testdir', 'file.txt')

>>> os.path.splitext('/path/to/file.txt')  # os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
('/path/to/file', '.txt')



*********************************Task******************************************

import os

[x for x in os.listdir('.') if os.path.isdir(x)]  # 列出当前目录下的所有目录
# Output:
'''
['.git', '.vscode', 'Python基础']  
'''

---------------------------------------------------------------------------
import os

[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

