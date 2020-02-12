class Myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x


obj=Myobject()
print(hasattr(obj,'x'))     # have attribute的简写
setattr(obj,'y',20)   #set attributed 的简写
print(obj.y)
print(getattr(obj,'y'))
print(obj.z)