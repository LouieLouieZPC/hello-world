class Father(object):
    def __init__(self,name):
        self.name=name
        print('hi')
    def get_name(self):
        return 'Father '+self.name

class Son(Father):
    def __init__(self, name):
        self.name=name
        print('hola')
    def get_name(self):
        return 'Son '+self.name

if __name__ == "__main__":
    son=Son('Frank')
    print(son.get_name())





