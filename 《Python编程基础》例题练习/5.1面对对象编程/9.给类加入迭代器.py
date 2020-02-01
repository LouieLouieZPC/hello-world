# 9.给类加入迭代器,需定义_iter_函数

class  Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info=[self.name,self.age]
        self.index=-1
    def getName(self):        # 函数：通过设置好的接口函数来访问对象
        return self.name
    def getAge(self):         # 函数：通过设置好的接口函数来访问对象
        return self.age
    def _iter_(self):         # 加入迭代器
        print('名字 年龄')
        return self
    def next(self):
        if self.index==len(self.info)-1:
            raise StopAsyncIteration
        self.index+=1
        return self.info[self.index]
newcat=Cat('coffe',3)         # 创建对象
print(newcat.getName())       # 通过设置好的接口函数来访问对象的属性
'''
结果如下：
coffe
'''
iterator=iter(newcat.next,1) # 调用迭代函数来输出对象的属性
for info in iterator:
    print(info)
'''
结果如下：
coffe
3
'''