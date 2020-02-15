# -*-coding:utf-8-*-

class Car():
    def __init__(self,brand,newWheelNum,newColor,T):
        self.brand=brand
        self.wheelNum=newWheelNum
        self.color=newColor
        self.T=T
        self.info=[self.brand,self.wheelNum,self.color,self.T]
        self.index=-1
    def getBrand(self):
        return self.brand
    def getNewheelnum(self):
        return self.wheelNum
    def getNewcolor(self):
        return self.color
    def getT(self):
        return self.T
    def __iter__(self):
        print('品牌 车轮数 颜色 废弃涡轮增压')
        return self
    def next(self):
        if self.index==3:
            raise StopIteration
        self.index+=1
        return self.info[self.index]
class Land_Rover(Car):
    def __init__(self,brand,newColor):        # 用构造函数创建对象
        self.brand=brand
        self.wheelNum=4
        self.color=newColor
        self.T=3
        Car.__init__(self,self.brand,self.wheelNum,self.color,self.T)    # 在子类中调用父类构造函数
Luxury_car=Car('BMW',4,'red',2.4)             # 创建类的对象
print(Luxury_car.getNewcolor())
iterator=iter(Luxury_car.next,1)              # 访问对象属性，调用iter函数
for i in iterator:
    print(i)

'''
以上结果为：
red
BMW
4
red
2.4
'''