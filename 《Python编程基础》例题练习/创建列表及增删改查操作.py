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

'''
month.append(元素)
month.extend(元素)
month.insert(位置,元素)
del month[位置]
month.pop(位置)
month.remove(元素)
'''

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
>>> month_copy=month.copy()                                       # 创建一个列表对象month的副本
>>> month_copy.pop(3)                                             # 使用pop函数获取并删除第4个元素
'April'
>>> del_element=month_copy.pop()                                  # 将最后一个元素赋值给一个变量并在副本中删除
>>> del_element                                                   # 查看删除元素
'None'
>>> month_copy                                                    # 查看副本
['January', 'February', 'March', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#3.14使用remove语句删除列表元素
>>> month.remove('None')                                          # 使用remove语句删除列表中的元素'None'
>>> month
['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#3.15
>>> month[0]='Jan'                                                # 将一个元素改成缩写形式
>>> month
['Jan', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


#3.16
>>> a=[1,2,3,4,]                                                  # 变量名a指向列表对象[1,2,3,4]
>>> b=a                                                           # 变量名b也指向列表对象[1,2,3,4]
>>> a.append(5)                                                   # 列表尾端追加元素5
>>> a                                                             # 通过变量b查看列表
[1, 2, 3, 4, 5]
>>> b                                                             # 通过变量b查看列表
[1, 2, 3, 4, 5]


#3.17
"""
# 使用copy方法创建副本:变量名1=变量名2.copy()
# 使用切片操作创建副本：变量名1=变量名2[:]
# 使用list函数创建副本：变量名1=list(变量名2)

"""
>>> a=[10,20,30,40,50]
>>> b=a.copy()                                                    # 使用copy方法创建副本:变量名1=变量名2.copy()
>>> c=a[:]                                                        # 使用切片操作创建副本：变量名1=变量名2[:]
>>> d=list(a)                                                     # 使用list函数创建副本：变量名1=list(变量名2)
>>> id(a);id(b);id(c);id(d)                                       # 查看变量对象id
1776541171328
1776570869824
1776570871040
1776570871552
>>> b[2]='three'                                                  # 修改副本第3个元素
>>> b
[10, 20, 'three', 40, 50]
>>> a                                                             # 原列表并没有发生变化
[10, 20, 30, 40, 50]
>>> c
[10, 20, 30, 40, 50]
>>> d
[10, 20, 30, 40, 50]


#3.18查询列表元素
>>> letter=['A','B','C','D','C','B','A']                          # 查询元素“C”在列表中的第一次出现的位置
>>> letter.index('C')
2
>>> 'D' in letter                                                 # 使用in函数判断列表是否包含元素
True


#3.19
>>> letter=['A','B','C','D','A','C','D','A']                      
>>> letter.count('A')                                             # 使用count函数进行元素计数，获取元素'A'在列表中出现的次数
3
>>> sorted(letter)                                                # 使用sorted函数对列表进行排序，不改变列表
['A', 'A', 'A', 'B', 'C', 'C', 'D', 'D']
>>> letter
['A', 'B', 'C', 'D', 'A', 'C', 'D', 'A']
>>> letter.sort()                                                 # 使用列表方法sort对列表进行排序，但会改变列表
>>> letter
['A', 'A', 'A', 'B', 'C', 'C', 'D', 'D']
>>> letter.sort(reverse=True)                                     # 使用列表方法sort对列表进行倒序排序，但会改变列表
>>> letter
['D', 'D', 'C', 'C', 'B', 'A', 'A', 'A']
>>> season=['spring','summer','autumn','winter']
>>> season.reverse()                                              # 使用reserve函数反转列表
>>> season
['winter', 'autumn', 'summer', 'spring']
>>> len(season)                                                   # 使用函数len获取列表长度
4
>>> [1,2,3]+[4,5,6]                                               # 使用列表加法合并两个列表
[1, 2, 3, 4, 5, 6]
>>> [1,2,3,4,5]*3                                                 # 使用列表乘法重复合并列表
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# 作业
>>> list1=[110,'dog','cat',120,'apple']                           # 定义变量
>>> list1.insert(2,[])                                            # 在第个二元素插入空列表
>>> list1
[110, 'dog', [], 'cat', 120, 'apple']
>>> list1.remove('apple')                                         # 删除元素
>>> list1
[110, 'dog', [], 'cat', 120]
>>> list1.index('cat')                                            # 查询元素位置
3
>>> list1[4]*=10                                                  # 提取元素，进行列表乘法重复运算以修改元素
>>> list1                                                         # 查看列表
[110, 'dog', [], 'cat', 1200]
>>> print(list1)                                                  # 输出列表
[110, 'dog', [], 'cat', 1200]