

class Father(object):
    def __init__(self,name):
        self.name=name
        print('hi')
    def get_name(self):
        return 'Father '+self.name
    def test(self):
        return('这是父类的方法')


class Son(Father):
    def __init__(self, name):
        self.name=name
        print('hola')
        Father.__init__(self,name)      # 重写了__init__ 时，但又继承了父类的构造方法
    def get_name(self):
        return 'Son '+self.name

if __name__ == "__main__":
    son=Son('Frank Yeats')
    print(son.test())
    print(son.get_name())


# Output:
hola
hi
这是父类的方法    # 子类继承且可调用父类的方法
Son Frank Yeats     # 重装，子类中的方法会覆盖父类中同名的方法