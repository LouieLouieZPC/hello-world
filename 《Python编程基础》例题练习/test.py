from types import MethodType

class Student(object):
    pass


def set_age(self,age):
    self.age=age


s=Student()
s.set_age=MethodType(set_age,s)  # 给实例添加方法
s.set_age(21)
print(s.age)

s=Student()
Student.set_age=MethodType(set_age,Student) # 给类添加方法
s.set_age(22)
print(s.age)

s=Student()
Student.set_age=set_age
s.set_age(23)
print(s.age)