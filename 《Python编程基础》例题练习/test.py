class Student(object):
    name='Frank'

s=Student()
print(s.name)
print(Student.name)
s.name=10
print(s.name)
print(Student.name)