# 5.22返回lambda语句创建函数
>>> example=lambda x:x**3         
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
>>> print(my_log(9))                        # 
2.0