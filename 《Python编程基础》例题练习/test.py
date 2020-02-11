class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')


a = list() # a是list类型
c = Dog() # c是Dog类型  

print(isinstance(a, list))

print(isinstance(c, Dog))
print(isinstance(c,Animal))