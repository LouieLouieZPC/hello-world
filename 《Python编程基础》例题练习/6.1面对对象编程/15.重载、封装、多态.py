# 重载：子类中的方法会覆盖父类中同名的方法
class Cat:
    def sayHello(self):
        print('mua------1')
class Bosi(Cat):
    def sayHello(self):
        print('mua------2')
Bosi=Bosi()
Bosi.sayHello()
'''
以上结果如下：
mua------2
'''

# 封装

# 多态