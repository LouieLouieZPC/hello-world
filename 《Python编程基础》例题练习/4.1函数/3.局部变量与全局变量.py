'''
定义在函数内部的变量拥有一个局部作用域，定义在函数外部的变量拥有全局作用域
'''
# 5.16 定义求和函数
def sum(*args):                # 定义函数(关键字可变参数)
    sum1=0
    for i in range(len(args)): # for循环
        sum1+=args[i]
    return sum1                # 返回运算结果变量
x=[12,87]
print('求和结果为：',sum(*x))