# 未私有化之前：可以直接在程序外部调用数据属性
print(cat1.age)
3
print(cat2.name)
Jack

'''
为防止程序开发人员无意中修改对象的状态，需要对类的数据属性和方法进行私有化
只需在在属性或方法名字前加下划线即可‘_’
'''



class Cat():
    def __init__(self,name,age):
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

print(cat1._Cat_name)
Tom
print(cat1._Cat_age)
3