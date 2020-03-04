import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))  # 默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可

# Output:
{"name": "Bob", "age": 20, "score": 88}