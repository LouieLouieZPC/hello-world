# -*-coding:utf-8-*-


class Car:
    def __init__(self,brand,WheelNum,Color,T):      # 构造器方法
        self.brand=brand                          # 属性
        self.WheelNum=WheelNum              # 属性
        self.Color=Color                    # 属性                       
        self.T=T                                  # 属性
    def run(self):                                # 方法(函数)
        print('车在跑，目标：夏威夷')
    def _del_(self):                              # 方法(函数)
        print('---解析方法被调用---')
info=Car('BMW',4,'red',2.4)                  # 创建对象，输入参数
print('车的颜色为：',   BMW.Color)   # 此类的数据属性与方法还未私有化，以此可以访问。访问对象的属性时，后面不用加括号
print('车轮子的数量为：',BMW.WheelNum) # 访问对象的属性时，后面不用加括号
print(BMW.run())     # 调用对象的run函数/方法，访问对象的方法时，后面需要加括号()，因为是有参数的
del BMW              # 删除对象
print(BMW)           # 查看对象是否被删除