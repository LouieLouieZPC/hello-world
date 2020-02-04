# 查询操作系统
>>> import os       # 导入模块
>>> os.name         # 获取当前操作系统
'nt'
>>> os.sep          # 查询文件路径的分隔符
'\\'
>>> os.linesep      # 查询当前系统使用的行终止符
'\r\n'

# 查询工作路径
>>> path=os.getcwd()
>>> print(path)
D:\01.Software\Python