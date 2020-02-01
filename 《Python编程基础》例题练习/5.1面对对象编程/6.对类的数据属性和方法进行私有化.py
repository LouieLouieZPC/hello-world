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
