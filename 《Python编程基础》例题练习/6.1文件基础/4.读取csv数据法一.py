'''
逗号分隔值有时也称为字符分隔值，我一种通用的、相对简单的文件格式，常应用于在程序之间转换表格数据。
常见的分隔符是逗号或者是制表号
编写时可考虑使用python的内置模块----csv模块
'''

# 7.25 读取iris数据法一：
import csv              # 调用csv模块
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\iris.csv'
with open(file_name,'r') as f:       # 打开，只读
    reader=csv.reader(f)             # 使用csv.reader函数（接收一个可迭代的对象，例.csv文件），能返回一个生成器，从中解析出csv的内容
    iris=[iris_item for iris_item in reader]     # 列表解析式
print(iris)
