class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):   # 把一个类当作
        return 'Student object (name:%s)'%self.name
    __repr__=__str__

s=Student('Yeats')
print(s)