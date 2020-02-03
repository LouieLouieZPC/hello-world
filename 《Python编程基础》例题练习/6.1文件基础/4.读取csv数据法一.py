# 7.25 读取iris数据法一：
import csv              # 调用csv模块
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\iris.csv'
with open(file_name,'r') as f:       # 打开，只读
    reader=csv.reader(f)             # 
    iris=[iris_item for iris_item in reader]
print(iris)
