class Father(object):
    def __init__(self,name):
        self.name=name
        print('name:%s'%self.name)
    def get_name(self):
        return 'Father '+self.name
class Son(Father):
    def get_name(self):
        return 'Son '+self.name

if __name__ == "__main__":
    son=Son('Yeats')
    print(son.get_name())



