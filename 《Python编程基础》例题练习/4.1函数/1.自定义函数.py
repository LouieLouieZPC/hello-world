'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。
所以最好用return替代print，return('xxxxx',xxxx)
函数可以同时返回多个值，但其实就是一个tuple。
函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

'''



#5.1 函数定义
>>> def my_function(parameter):        # del关键词（即definition） 函数名（形参）:
...  '打印任何传入的字符串'
...  print(parameter)
...  return 'parameter is '+parameter    # 返回函数值

# 5.2 默认参数
>>> def interest(money,day=1,interest_rate=0.05):      # 定义这么个函数,对以下整段程序逻辑封装
...  income=0
...  income=money*interest_rate*day/365
...  print(income)
# 5.3 默认参数使用
>>> interest(5000)               
0.684931506849315
>>> interest(money=5000)           # 关键字参数调用
0.684931506849315
>>> interest(10000)
1.36986301369863



# 5.4 任意数量的位置可变参数
'''
*和**
实际上真正的Python参数传递语法是*和**。
*args和**kwargs只是一种约定俗成的编程实践。我们也可以写成*vars和**kvars。

*args和**kwargs一般是用在函数定义的时候。二者的意义是允许定义的函数接受任意数目的参数。
也就是说我们在函数被调用前并不知道也不限制将来函数可以接收的参数数量。

*args用来表示函数接收可变长度的非关键字参数列表作为函数的输入，存储在元组中。
**kwargs表示函数接收可变长度的关键字参数字典作为函数的输入。

'''
>>> def exp(x,y,*args):         # 定义函数
...  print('x:',x)
...  print('y:',y)
...  print('args:',args)
...
>>> exp(1,5,66,55,'abc')
x: 1
y: 5
args: (66, 55, 'abc')           # *args参数传入函数后存储在元组中



# 5.5 任意数量的关键字可变参数
>>> def exp(x,y,*args,**kwargs):
...  print('x:',x)
...  print('y:',y)
...  print('args:',args)
...  print('kwargs:',kwargs)
...
>>> exp(1,2,2,4,6,a='c',b=1)
x: 1
y: 2
args: (2, 4, 6)
kwargs: {'a': 'c', 'b': 1}



# 5.6 return函数
>>> def interest_r(money,day=1,interest_rate=0.05):
...  income=0
...  income=money*interest_rate*day/365
...  return income

# 5.7print和return的区别
>>> x=interest(1000)        
0.136986301369863
>>> x                   # print函数仅仅是直接打印了对象，打印出来的结果没有被保存在x里，无法调用

>>> y=interest_r(1000)
>>> y
0.136986301369863       # print函数返回的结果保存在y中，可供其他函数调用



# 5.8 传入位置参数
>>> list(range(0,10,2)) # 按start=0,stop=10,step=2的顺序传入
[0, 2, 4, 6, 8]
>>> list(range(10,0,2)) # 调转start和stop的顺序后传入
[]
>>> list(range(10,2,0)) # 调转全部参数的顺序后报错（位置参数顺序不可调换）
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: range() arg 3 must not be zero



# 5.9 调用位置参数
>>> list(range(0,10,1))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10))             # 当函数的参数有默认设置值时，可以不设置该函数会自动用默认值
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# 5.10 设置关键字参数
>>> def interest(money,day=1,interest_rate=0.05):      # 定义这么个函数,对以下整段程序逻辑封装
...  income=0
...  income=money*interest_rate*day/365
...  print(income)
>>> interest(money=5000,day=7,interest_rate=0.06)
5.7534246575342465
>>> interest(money=7,day=5000,interest_rate=0.06)
5.7534246575342465
# 5.11 调用关键字参数
>>> interest(10000,day=7,interest_rate=0.06)
11.506849315068493
>>> interest(10000,interest_rate=0.06,day=7)
11.506849315068493
>>> interest(interest_rate=0.06,7,money=10000)       # money为位置参数，其他未关键字参数
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument  # 犯了位置参数跟在关键字参数后面的错误



# 5.12 调用*arg可变参数
# >>> arg=[0,10,2]
>>> list(range(*arg))              # *arg可以直接将元组或者列表转换为参数
[0, 2, 4, 6, 8] 


#5.13 调用**kwargs可变参数
>>> def user(username,age,**kwargs):                    # 定义函数（位置参数，位置参数，关键字可变参数）
...  print('uesrname:',username)
...  print('age:',age)
...  print('other:',kwargs)
...
>>> user('john',27,city='guangzhou',job='Date Analyst')
uesrname: john
age: 27
other: {'city': 'guangzhou', 'job': 'Date Analyst'}
>>> kw={'age':27,'city':'guangzhou','job':'Date Analyst'}
>>> user('john',**kw)                                   # 调用**关键词可变参数 
uesrname: john
age: 27
other: {'city': 'guangzhou', 'job': 'Date Analyst'}
