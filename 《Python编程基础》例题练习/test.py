class Father(object):
    def __init__(self,name):
        self.name=name
        print('name:%s'%self.name)
    def get_name(self):
        return 'Father '+self.name
    def test(self):
        return('这是父类的方法')

class Son(Father):
    def get_name(self):
        return 'Son '+self.name

if __name__ == "__main__":
    son=Son('Yeats')         # 创建子类对象
    print(son.test())
    print(son.get_name())    

# Output:
name:Yeats       # 子类中没有构造方法，以此默认调用父类的构造方法
这是父类的方法    # 子类继承且可调用父类的方法
Son Yeats        # 重装，子类中的方法会覆盖父类中同名的方法