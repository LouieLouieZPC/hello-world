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
    def get_name(self):
        return 'Son '+self.name

if __name__ == "__main__":
    son=Son('Frank')
    print(son.test())
    print(son.get_name())

# Output:
hola    # 如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__
这是父类的方法    # 子类继承且可调用父类的方法
Son Frank  # 重装，子类中的方法会覆盖父类中同名的方法


