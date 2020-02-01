class Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def _sleep_(self):
        print('%d岁的%s正在沙发上睡懒觉。'%(self.age,))
    def _eat_(self,food):
        self.food=food
        print('%d岁的%s正在吃%s。'%(self.age,self.name,self.food))
cat1=Cat('Tom',3)                 # 创建对象cat1
cat2=Cat('Jack',4)                # 创建对象cat1
print('Cat1的名字为：',cat1.name) 
Cat1的名字为： Tom
print('Cat2的名字为：',cat2.name)
Cat2的名字为： Jack