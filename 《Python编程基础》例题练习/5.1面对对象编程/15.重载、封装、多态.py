# -*-coding:utf-8-*-

class Car():
    def __init__(self,newWheelNum,newColor,T):
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
        return
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
