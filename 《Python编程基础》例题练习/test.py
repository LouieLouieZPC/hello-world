from types import MethodType

class Student(object):
    __slots__=('name','age')



def set_age(self,age):
    self.age = age
def set_score(self,score):
    self.score = score

    
s=Student()
s.gender='male'
print(s.gender)


