#-*-coding:utf-8-*-

class Car():
    '一次模拟汽车的简单尝试'
    wheelNum=4           # 增加属性
    color='red'          # 增加属性
    def getCarInfo(self,name):         # name作为一个位置参数
        self.name=name                 # 参数name可以用进运算也可不用进，具体情况具体分析
        print('%s有%d个车轮，颜色是%s'%(self.name,self.wheelNum,self.color))        # 调用属性也会用到self.
    def run(self):
        print('老司机正在开车！！！')
new_car=Car()                                # bart指向Car的实例/对象，即self,self即实例本身
print(new_car.getCarInfo('我的奔驰'))         # name作为一个位置参数在被调用时是要设置值滴！
print(new_car.run())
