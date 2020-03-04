'''
将字典数据写入文件：

准备好一个键的列表
打开，'w',newline=''
x=csv.DictWriter(可迭代对象,键的列表)
x.writeheader()        # 用csv.writerheader函数输入标题
x.writerows(列表数据)   # 将列表数据写入列表,writerow需要一个可迭代的单元格来编写

'''
import csv
file_name=r'\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1文件基础\iris.csv'
with open(file_name,'r') as f:
    reader=csv.DictReader(f)         # 使用csv.DictReader函数（接收一个可迭代的对象，例.csv文件），能返回一个生成器，但是返回的每一个单元格都放在一个字典的值内，而字典的键则是这个单元格的标题
    isir1=[iris_item for iris_item in reader]     # 列表解析式
# 将字典数据写入csv文件
import csv
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1文件基础\text.csv'
my_key=[]                      # 创建一个键的集合
for i in isir1[1].keys():      # 获取第一个字典内的所有键
    my_key.append(i)           # 键键添加进集合内
with open(file_name,'w',newline='') as f:       # 打开，写入
    write_csv=csv.DictWriter(f,my_key)           # 使用csv.Dictwriter函数（接收一个可迭代的对象，例.csv文件，输入字典所有键的数据）
    write_csv.writeheader()                      # 使用csv.writerheader函数输入标题
    write_csv.writerows(isir1)                        # 使用csv.writerrows函数将列表数据写入列表,writerow需要一个可迭代的单元格来编写