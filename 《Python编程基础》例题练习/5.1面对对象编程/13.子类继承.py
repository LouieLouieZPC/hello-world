class Cat():
    def __init__(self):
        self.name='猫'
        self.age=4
        self.info=[self.name,self.age]
        self.index=-1
    def run(self):
        print(self.name,'--is runing')
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def _iter_(self):
        print('名字 年龄')
        return self
    def next(self):
        if self.index==len(self.info)-1:
            raise StopIteration
        self.index+=1
        return self.info[self.index]
class Bosi(Cat):
    def setName(self,newName):
        self.name=newName
    def eat(self):
        print(self.name,'--is eating')
bs=Bosi()
print('bs的名字是：',bs.name)
print('bs的年龄为：',bs.age)
print(bs.run())
bs.setName('波斯猫')
bs.eat()
iteration=iter(bs.next,1)
for info in iteration:
    print(info)