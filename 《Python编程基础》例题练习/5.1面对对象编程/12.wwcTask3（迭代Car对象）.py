# -*-coding:utf-8-*-


class Car:
    def __init__(self,brand,WheelNum,Color,T):      # 构造器方法
        self.brand=brand                          # 属性
        self.WheelNum=WheelNum              # 属性
        self.Color=Color                    # 属性                       
        self.T=T                                  # 属性
        self.info=[self.brand,self.WheelNum,self.Color,self.T]
        self.index=-1
    def getBrand(self):                            # 方法(函数)
        return self.brand
    def getWheelNum(self):                         # 方法(函数)
        return self.WheelNum
    def getColor(self):                            # 方法(函数)
        return self.Color
    def getT(self):                                # 方法(函数)
        return self.T
    def _iter_(self):                               # 方法(函数)
        print('品牌 车辆数 颜色 废气涡轮增压')
        return self
    def next(self):
        if self.index==3:
            raise StopIteration
        self.index+=1
        return  self.info[self.index]

newcar=Car('BMW',4,'red',2.4)                  # 创建对象，输入参数
print('车的颜色为：',newcar.Color)              # 此类的数据属性与方法还未私有化，以此可以访问。访问对象的属性时，后面不用加括号
iterator=iter(newcar.next,1)
for info in iterator:
    print(info)