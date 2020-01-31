class Cat():
    '再次模拟猫咪的简单尝试'
    def __init__(self,name,age):  # 用构造器初始化类的实例对象 
        self.name=name            # 属性
        self.age=age              # 属性
    def sleep(self):
        print('%d岁的%s正在沙发上睡懒觉。'%(self.age,self.name))
    def eat(self,food):
        self.food=food
        print('%d岁的%s正在吃%s'%(self.age,self.name,self.food))
