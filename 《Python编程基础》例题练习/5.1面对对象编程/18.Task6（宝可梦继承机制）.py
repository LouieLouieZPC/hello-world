class Pokemon():
    def __init__(self):      #初始化      ,没用到参数，不用加
        self.name='小火龙'    #设置小火龙角色的属性
        self.gender='雄性'    #设置小火龙角色的属性
        self.level=0          #设置小火龙角色的属性
        self.type='电'         #设置小火龙角色的属性
        self.status=[13,5,5,5,5,5]   #设置小火龙角色的属性
        self.info=[self,self.name,self.type,self.gender,self.level,self.status]
        self.index=-1
    def getName(self):
        return self.name
    def getGender(self):
        return self.gender
    def getStatus(self):
        return self.status
    def getType(self):
        return self.type
    def level_up(self):
        for x in range(len(self.status)):
            self.status[:]+=1
            self.status[0]+=1
            return self.status
    def __iter__(self):
        print('名字 属性 性别 等级 能力')
        return self
    def next(self):
        if self.index==5:
            raise StopIteration
        self.index+=1
        return self.info[self.index]

class Charmander(Pokemon):
    def setName(self,newName):
        self.name=newName

pokemon1=Pokemon()                   # 创建子类的对象，调用了父类的__init__函数，并向父类传输数据
print(pokemon1.status)               # 访问父类属性
iterator=iter(pokemon1.next,1)       # iter(object, sentinel)创建迭代器对象，迭代输出父类的属性
for i in iterator:                   # 遍历迭代器对象的同时每次都会调用next函数
    print(i)
 
'''
以上结果如下：
小火龙
电
雄性
0
[13, 5, 5, 5, 5, 5]
'''