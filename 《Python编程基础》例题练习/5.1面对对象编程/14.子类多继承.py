class A(object):
    def __init__(self):
        print('  ->Input A')
        print('  <-Output A')
class B(A):
    def __init__(self):
        print('  ->Input B')
        A.__init__(self)
        print('  <-Output B')
class C(A):
    def __init__(self):
        print('  ->Input C')
        A.__init__(self)
        print('  <-Output C')
class D(B,C):
    def __init__(self):
        print('  ->Input D')
        B.__init__(self)
        C.__init__(self)
        print('  <-Output D')