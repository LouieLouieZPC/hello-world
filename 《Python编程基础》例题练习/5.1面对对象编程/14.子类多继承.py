class A(object):
    def __init__(self):         # 定义一个父类  
        print('  ->Input A')
        print('  <-Output A')
class B(A):                     # 定义一个子类
    def __init__(self):
        print('  ->Input B')
        A.__init__(self)
        print('  <-Output B')
class C(A):                     # 定义一个子类
    def __init__(self):
        print('  ->Input C')
        A.__init__(self)
        print('  <-Output C')
class D(B,C):                   # 定义一个子类
    def __init__(self):
        print('  ->Input D')
        B.__init__(self)
        C.__init__(self)
        print('  <-Output D')
d=D()                         # python中是可以多继承的，子类会继承父类中的方法、属性
print(issubclass(C,B))        # issubclass() 方法的语法:issubclass(class, classinfo).如果 class 是 classinfo 的子类返回 True，否则返回 False。
print(issubclass(C,A))        # 判断一个类是不是另一个类的子类  

'''
以上结果如上：
  ->Input D
  ->Input B
  ->Input A
  <-Output A
  <-Output B
  ->Input C
  ->Input A
  <-Output A
  <-Output C
  <-Output D
False
True
'''