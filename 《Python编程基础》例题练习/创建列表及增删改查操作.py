# 3.1
>>> mylist1=[1,2.0,['three','four',5],6.5,True]          # 创建包含混合数据类型的嵌套列表
>>> mylist1                                              # 查看列表内容
[1, 2.0, ['three', 'four', 5], 6.5, True]
>>> empty_list=[]                                        # 创建空列表
>>> empty_list
[]

# 3.2
>>> mylist=list((1,2.0,['three','four',5],6.5,True))     # 向list函数传入一个对象
>>> mylist
[1, 2.0, ['three', 'four', 5], 6.5, True]
>>> type(mylist)                                         # 用type()查看对象的数据类型
<class 'list'>
>>> empty_list=list()                                    # 创建空列表
>>> empty_list
[]
>>> mylist1=list(['one','two','three'])                  # 向list函数传入一个列表对象
>>> mylist1
['one', 'two', 'three']

# 3.3
>>> list('hello world!')                                 # 向函数list传入一个字符串
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']

#3.4
>>> mylist=['Sunday','Monday','Tuesday','Wednesday','thursday','Friday']
>>> mylist[1]                                            # 提取列表中第二个元素
'Monday'
>>> mylist[-3]                                           # 提取列表中倒数第三个元素
'Wednesday'

#3.5
>>> mylist[7]                                            # 传入的索引大于最后一个元素的正索引
Traceback (most recent call last):                       # 追溯
  File "<stdin>", line 1, in <module>
IndexError: list index out of range                      # 列表索引超出范围
>>> mylist[-10]                                          # 传入的索引小于第一个元素的负索引
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

#3.6
# 步长为正数时的切片操作
>>> mylist=[10,20,30,40,50,60,70,80,90,100]
>>> mylist[2:7]
[30, 40, 50, 60, 70]                   # 提取从第2~8个元素之间的元素
>>> mylist[1:9:2]                      # 提取从第1~10个元素之间的元素，步长为2
[20, 40, 60, 80]
# 步长为负数时的切片操作
>>> mylist[-2:-8:-2]                   # 提取倒数第1~8个元素之间的元素，步长为2
[90, 70, 50]
# 步长为0时会报错
>>> mylist[1:4:0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: slice step cannot be zero

#3.7
>>> mylist=[10,20,30,40,50,60,70,80,90,100]
# 省略起始索引
>>> mylist[:-7:-2]       # 提取从结尾向左到倒数第7个元素前的所有元素，步长为2
[100, 80, 60]
# 省略终止索引
>>> mylist[6:]           # 提取从第7个元素到列表右端最后一个元素之间所有元素，步长默认为1
[70, 80, 90, 100]
# 同时省略起始和终止索引
>>> mylist[::-2]         # 提取从右端开始到左端之间的所有元素，步长为2
[100, 80, 60, 40, 20]
>>> mylist[::-1]         # 提取从右端开始到左端之间的所有元素，步长为1，即列表反转
[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

#3.8
>>> mylist=[10,20,30,40,50,60,70,80,90,100]
>>> mylist[-2:4:1]
[]                       # 返回一个空列表
>>> mylist[3:100:2]      # 提取从第4个元素到右端之间的全体元素，步长为2
[40, 60, 80, 100]
>>> mylist[-5:-20:-1]    # 提取从倒数第5个元素到左端之间的全体元素，步长为1
[60, 50, 40, 30, 20, 10]
>>> mylist[6:2]          # 提取从第7个元素向右到第三个元素之间的所有元素
[]                       # 返回一个空列表

#3.9 追加元素
>>> month=['January','February','March','April','May','June']
>>> month.append('July')                                          # 使用append函数向列表尾部追加元素
>>> month                                                         # 查看列表内容
['January', 'February', 'March', 'April', 'May', 'June', 'July']
#3.10追加多个元素
>>> month_copy=month.copy()                                       # 使用copy函数创建一个列表对象month的副本，理由稍后解释
>>> month_copy
['January', 'February', 'March', 'April', 'May', 'June', 'July']
>>> others=['August','September','November','December']
>>> month.extend(others)                                          # 使用extend函数将两个列表进行合并
>>> month
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']
>>> month_copy+=others                                            # 使用加法赋值运算符(+=)对副本进行自增运算
>>> month_copy
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']
#3.11 插入元素
>>> month.insert(9,'October')                                     # 使用insert函数在列表第10个位置上插入元素'October'
>>> month
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
>>> month.insert(20,'None')                                       # 插入位置超出列表尾端
>>> month
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'None']
#使用del语句删除元素
>>> month_copy=month.copy()                                       # 使用copy函数创建列表对象month的副本
>>> del month_copy[-1]                                            # 用del语句删除副本最后一个元素
>>> month_copy
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#3.13 使用pop语句删除元素
'''
month.append(元素)
month.extend(元素)
month.insert(位置,元素)
del month[位置]
month.pop(位置)
month.remove(元素)
'''