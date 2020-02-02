class Cat():
    def __init__(self):                    # 初始化（子类不需要，只需一个）
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
bs=Bosi()                                     # 创建子类的对象
print('bs的名字是：',bs.name)                  # 此父类的数据属性与方法还未私有化，以此可以访问。该子类继承了父类的属性和方法。访问对象的属性时，后面不用加括号
print('bs的年龄为：',bs.age)                   # 访问父类属性
print('bs的年龄为：',bs.getAge())              # 
print(bs.run())
bs.setName('波斯猫')                           # 访问子类的属性和方法
bs.eat()
iteration=iter(bs.next,1)                     # iter(object, sentinel)创建迭代器对象
for info in iteration:                        # 遍历迭代器对象的同时每次都会调用next函数
    print(info)