# -*-coding:utf-8-*-
'''
访问对象的属性时，后面不用加括号
访问对象的方法/函数时，后面需要加括号()，因为它是个函数，且是有参数的

'''
class Car:
    def __init__(self,newWheelNum,newColor):      # 构造器方法
        self.newWheelNum=newWheelNum              # 属性
        self.newColor=newColor                    # 属性
    def run(self):                                # 方法(函数)
        print('车在跑，目标：夏威夷')
    def _del_(self):                              # 方法(函数)
        print('---解析方法被调用---')
BMW=Car(4,'red')            # 创建对象，输入参数
print(BMW)                  # 查看对象
print('车的颜色为：',   BMW.newColor)   # 此类的数据属性与方法还未私有化，以此可以访问。访问对象的属性时，后面不用加括号
print('车轮子的数量为：',BMW.newWheelNum) # 访问对象的属性时，后面不用加括号
print(BMW.run())     # 调用对象的run函数/方法，访问对象的方法时，后面需要加括号()，因为是有参数的
del BMW              # 删除对象
print(BMW)           # 查看对象是否被删除

'''
以上结果如下：
<__main__.Car object at 0x0000020637721730>
车的颜色为： red
车轮子的数量为： 4
车在跑，目标：夏威夷
None
Traceback (most recent call last):
  File "d:/01.Software/GitHub/GitHub Repository/hello-world/《Python编程基础》例题练习/5.1面对对象编程/7.Task2（创建Car对象）.py", line 21, in <module>
    print(BMW)           # 查看对象是否被删除
NameError: name 'BMW' is not defined

'''