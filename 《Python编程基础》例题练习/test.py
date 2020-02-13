class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value
    def __str__(self):
        return '[Value: %s]' % self.data
    __repr__=__str__
    

ts =Test()
ts

print ts
