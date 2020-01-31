# 5.22返回lambda语句创建函数
>>> example=lambda x:x**3         # lambda 参数:返回值
>>> print(example)
<function <lambda> at 0x00000242938D0160>
>>> example(2)
8


# 5.23使用lambda语句创建对数函数
>>> from math import log                    # 引如math数学库的对数函数
>>> def make_logarithmic_function(base):    # 此函数用于返回一个以base为底的匿名对数函数
...  return lambda x:log(x,base)            # 返回一个以base为底，以x为真数的匿名对数函数
...
>>> my_log=make_logarithmic_function(3)     # （python允许将lambda语句作为对象赋值给变量，然后使用变量名进行调用）调用匿名函数my_log，底数已经设置为默认参数3，x为位置参数)
>>> print(my_log(9))                        # 设置位置参数x=9
2.0                                         # y=log(9,3)=2.0



# 5.24使用map函数实现代码5.22
def add(x):                                # 定义函数
    x+=3
    return x
numbers=list(range(10))
num1=list(map(add,numbers))                # map（函数，序列）
num2=list(map(lambda x:x+3,numbers))       # 速度更快，可读性更强
>>> num1
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]          
>>> num2
[3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 


# 5.25 fib函数示例
def fib(n):
    if n<=2:
        return 2
    else:
        return fib(n-1)+fib(n-2)
f=fib(10)
print(f)
110


# 5.26 filter函数示例
list(filter(lambda x：x%2==1,[1,4,6,7,9,12,17]))
s=list(filter(lambda c:c!='o','I love python and R!'))
s='',join(s)
print(s)
['I', ' ', 'l', 'v', 'e', ' ', 'p', 'y', 't', 'h', 'n', ' ', 'a', 'n', 'd', ' ', 'R', '!']

