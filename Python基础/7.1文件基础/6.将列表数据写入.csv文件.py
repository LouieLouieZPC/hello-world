'''
将列表数据逐行写入csv文件：
打开，'w',newline=''             # newline=''是选择空行的意思
x=csv.writer(可迭代对象)    # 创建csv库writer类的对象
x.writerow(列表数据)    # 调用对象函数writerow,将列表数据逐行写入对象
'''

# 读取csv文件
import csv              # 调用csv模块
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1文件基础\iris.csv'
with open(file_name,'r') as f:       # 打开，只读
    reader=csv.reader(f)             # 使用csv.reader函数（接收一个可迭代的对象，例.csv文件），能返回一个生成器，从中解析出csv的内容
    iris=[iris_item for iris_item in reader]     # 列表解析式
print(iris)


# 将列表数据写入csv文件
import csv      # 调用csv模块
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1文件基础\text.csv'
with open(file_name,'w',newline='') as f:       # 打开，写入
    write_csv=csv.writer(f)           # 创建csv库writer类的对象，使用csv.writer函数（接收一个可迭代的对象，例.csv文件）
    write_csv.writerow(iris)          # 调用对象函数writerow，使用csv.writerrow函数将列表数据逐行写入对象