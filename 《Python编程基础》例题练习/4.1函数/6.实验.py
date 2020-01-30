def add(x):
    x+=3
    return x
numbers=list(range(10))
num1=list(map(add,numbers))
num2=list(map(lambda x:x+3,numbers))