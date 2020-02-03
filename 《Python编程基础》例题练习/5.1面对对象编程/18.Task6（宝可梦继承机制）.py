class Charmander():
    def __init__(self,name,gender,level,type,status):
        self.name=name
        self.gender=gender
        self.level=level
        self.type=type
        self.status=status
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
pokemon1=Charmander('皮卡丘','雄性',0,'电',[10,5,5,5,5,5])
iterator=iter(pokemon1.next,1)
for i in iterator:
    print(i)

