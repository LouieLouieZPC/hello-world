class  Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info=[self.name,self.age]
        self.index=-1         # 为迭代设置初始变量
    def getName(self):        # 函数：通过设置好的接口函数来访问对象
        return self.name
    def getAge(self):         # 函数：通过设置好的接口函数来访问对象
        return self.age
    def __iter__(self):         # 加入迭代器
        print('名字 年龄')
        return self           # __iter__() 方法返回一个特殊的迭代器对象,实例本身就是迭代对象，故返回自己
    def __next__(self):
        if self.index==len(self.info)-1:
            raise StopAsyncIteration
        self.index+=1
        return self.info[self.index]
newcat=Cat('coffe',3)         # 创建类的对象
print(newcat.getName())       # 通过设置好的接口函数来访问对象的属性

for info in Cat():
    print(info)