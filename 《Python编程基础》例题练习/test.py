from functools import wraps

def log(func1):    # 此为高阶函数
    if isinstance(func1,str):   # 若高阶函数传入的参数是字符串，则可用isinstance判断
        def decorator(func2):   # 声明一个装饰器函数
            @wraps(func2)
            def wrapper(*args,**kw):
                print('%s begin call %s'%(func1,func2.__name__))
                func2(*args,**kw)
                print('%s end call %s'%(func1,func2.__name__))
                return func2(*args,**kw)
            return wrapper
        return decorator   # 第一种情况，这是一个返回decorator（装饰器）的高阶函数
    else:
        @wraps(func1)
        def wrapper(*args,**kw):  # 第二种情况，无需声明再装饰器函数，该高阶函数即为装饰器函数
            print('begin call %s'%func1.__name__)
            func1(*args,**kw)
            print('end call %s'%func1.__name__)
            return func1(*args,**kw)
        return wrapper


@log
def f():
    pass

f()
# Output:
begin call f
end call f





@log('execute')    # 先给log函数传入字符串类型的参数'execute'，再给它传入函数类型的参数f()
def x():
    pass

x()
# Output:
execute begin call x
execute end call x