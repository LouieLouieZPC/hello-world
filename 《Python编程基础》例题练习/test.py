def count():
    fs = []
    for i in range(1, 4):     # 循环变量i
        def f():
             return i*i       # 此处引用了循环变量
        fs.append(f)
    return fs


def count():
    def n(x):
        def n1():
            return x*x
        return n1
    n2=[]
    for i in range(1,4):
        n2.append(n(i)) 
    return n2

f1, f2, f3 = count()
print(f1(),f2(),f3())