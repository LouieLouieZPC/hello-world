# -*-coding:utf-8-*-
'''
访问对象的属性时，后面不用加括号
访问对象的方法时，后面需要加括号()，因为是有参数的

'''
class Car:
    def __init__(self,newWheelNum,newColor):
        self.newWheelNum=newWheelNum
        self.newColor=newColor
    def run(self):
        print('车在跑，目标：夏威夷')
    def _del_(self):
        print('---解析方法被调用---')
BMW=Car(4,'red')
print(BMW)
print('车的颜色为：',   BMW.newColor)   # 此类的数据属性与方法还未私有化，以此可以访问。访问对象的属性时，后面不用加括号
print('车轮子的数量为：',BMW.newWheelNum) # 访问对象的属性时，后面不用加括号
print(BMW.run())     # 调用对象的run函数/方法，访问对象的方法时，后面需要加括号()，因为是有参数的
del BMW              # 删除对象
print(BMW)           # 查看对象是否被删除
