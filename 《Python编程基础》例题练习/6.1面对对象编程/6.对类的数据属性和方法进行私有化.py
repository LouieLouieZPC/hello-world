# 未私有化之前：可以直接在程序外部调用数据属性
print(cat1.age)
3
print(cat2.name)
Jack

'''
为防止程序开发人员无意中修改对象的状态，需要对类的数据属性和方法进行私有化
只需在在属性或方法名字前加双下划线即可‘_’
'''

class Cat():
    def __init__(self,name,age):      # __init__是特殊变量，特殊变量是可以直接访问的,不是private变量
        self._name=name
        self._age=age
    def sleep(self):
        print('%d岁的%s正在沙发上睡懒觉。'%(self._age,self._name))
    def eat(self,food):
        self._food=food
        print('%d岁的%s正在吃%s。'%(self._age,self._name,self._food))
    def getAttribute(self):
        return self._name,self._age
cat1=Cat('Tom',3)      # 创建对象，输入参数
cat2=Cat('Jack',4)     # 创建对象，输入参数
print('Cat1的名字为：',cat1.name)         # 私有化后从外部访问对象的属性会发现访问不了
Traceback (most recent call last):      
  File "d:/01.Software/GitHub/GitHub Repository/hello-world/《Python编程基础》例题练习/5.1面对对象编程/6.对类的数据属性和方法进行私有化.py", line 23, in <module>
    print('Cat1的名字为：',cat1.name)
AttributeError: 'Cat' object has no attribute 'name'
print(cat1.sleep())           # 只能通过设置好的接口函数来访问对象
# 结果为：3岁的Tom正在沙发上睡懒觉。
print(cat2.eat('fish'))       # 只能通过设置好的接口函数来访问对象
# 结果为：4岁的Jack正在吃fish。
print(cat1.getAttribute())    # 只能通过设置好的接口函数来访问对象
# 结果为：('Tom',3)


'''
事实上想从外部访问这些私有数据属性也是可以的:
name_mangling技术
'''




通过设置好的接口函数来访问对象原理：
面向对象编程的一个重要特点就是数据封装。
既然Cat实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Cat类的内部定义访问数据的函数，
这样，就把“数据”给封装起来了。这些封装数据的函数是Cat类本身是关联起来的，我们称之为类的方法






**************************************************************************************
Task:

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,new_gender):
        if (new_gender !='male') and (new_gender !='female'):
            raise ValueError('bad gender!!!Are you human?')
        else:
            self.__gender=new_gender


# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')