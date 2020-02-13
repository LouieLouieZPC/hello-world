class Student(object):
    def __init__(self):
        self.name='frank'
    def __getattr__(self,attr):
        if attr=='age':
            return '21 years'
        raise AttributeError('\'Student has not attribute %s '%attr)

s=Student()
print(s.name)
print(s.age)
print(s.gender)