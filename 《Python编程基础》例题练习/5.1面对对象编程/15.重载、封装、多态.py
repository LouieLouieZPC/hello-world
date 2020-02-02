# 重载
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