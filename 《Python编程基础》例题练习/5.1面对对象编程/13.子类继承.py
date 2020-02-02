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
        if self.index==len(self.info)-1:
            raise StopIteration
        self.index+=1
        return self.info[self.index]