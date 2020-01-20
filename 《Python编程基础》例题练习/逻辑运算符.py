>>> a=11,;b=22;print('a=11,b=22')        # 初始赋值
a=11,b=22
>>> print('a and b=',a and b);print('a or b=',a or b);print('not a=',not a);print('not b=',not b);print('not(a and b)=',not(a and b))
a and b= 22                              # 一假为假（and运算符必须确保所有的运算数都是True才会把所有的运算数都解析，并且返回最后一个变量）
a or b= 11                               # 一真为真（or运算符，即只要有一个为True，即停止解析运算符返回最近为True的变量）
not a= False
not b= False
not(a and b)= False

>>> a=0;b=22;print('a=0,b=22')           # 重新赋值
a=0,b=22
>>> print('a and b=',a and b);print('a or b=',a or b);print('not a=',not a);print('not b=',not b);print('not(a and b)',not(a and b))
a and b= 0
a or b= 22
not a= True
not b= False
not(a and b) True

# 下面是用按位运算符和逻辑运算符用于bool值运算时，俩效果是一样的
>>> True & True;True and True;True & False;True and False        # 按位&、逻辑and（一假为假）
True
True
False
False
>>> True | False;True or False;False | False;False or False      # 按位|、逻辑or（一真为真）
True
True
False
False