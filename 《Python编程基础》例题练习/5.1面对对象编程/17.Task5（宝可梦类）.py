class Charmander(object):
    def __init__(self,name,gender,level,status,type)
    self.name=name
    self.gender=gender
    self.level=level
    self.status=status
    self.type=type
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
    def __iter__(self):
        print('名字 属性 性别 等级 能力')
        return self
    def next(self):
        if self.index==4:
            raise StopIteration
        self.index+=1
        return self.info[self.index]
pokemon1=