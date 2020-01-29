'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外部的变量拥有全局作用域
'''
# 5.16 定义求和函数————局部变量（仅在函数体内有效）
def sum(*args):                # 定义函数(关键字可变参数)
    sum1=0                     # 定义局部变量
    for i in range(len(args)): # for循环
        sum1+=args[i]
    return sum1                # 返回运算结果变量
x=[12,87]
print('求和结果为：',sum(*x))

# 5.18全局变量（可以在函数体内被调用）
sum0=10                        # 此为全局变量
def fun():
    sum_global=sum0+100        # 此为局部函数
    return sum_global          # 返回运算结果
print('结果为',fun())

# 5.19全局变量不能在函数体中被直接赋值
sum1=0                             # 此为全局变量
def sum(*arg):
    for i in range(len(arg)):
        sum1+=arg[i]               # 全局变量不能在函数体中被直接赋值
    return sum1
>>> sum(1,2,3,4)
Traceback (most recent call last):            # 全局变量不能在函数体中被直接赋值，否则会报错
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in sum
UnboundLocalError: local variable 'sum1' referenced before assignment


# 5.20局部变量覆盖全局变量————（若同时存在全局变量和局部变量，函数体会使用局部变量将全局变量进行覆盖）
sum1=10                   # 定义全面变量
def sum(*arg):            # 定义函数
    sum1=0                # 定义局部变量
    for i in range(len(arg)):  # for循环语句迭代所有元素索引
        sum1+=arg[i]        
    return sum1            # 返回局部变量
sum(1,3,4,5)               # 运算结果为13


# 5.21使用关键字global在函数体内对全局变量赋值
sum1=0
def sum(*arg):
    global sum1            # 使用关键字global后，可在函数体内对全局变量sum1赋值
    for i in range(len(arg)):
        sum1+=arg[i]
    return sum1
>>> sum(1,3,5,7)
16
>>> sum1
16
>>> sum(1,3,5,7)
32

