import functools
def log01(text=None):   # 默认参数为None
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text is not None:
                print('%s begin call %s()' % (text, func.__name__))
                fu = func(*args, **kw)
                print('%s end call %s()' % (text, func.__name__))
            else:
                print('begin call %s()' % func.__name__)
                fu = func(*args, **kw)
                print('end call %s()' % func.__name__)
            return fu

        return wrapper

    return decorator


@log01()  # 这种方法必须加(), 不能直接写@log01
def test1(n):
    print('这里是%sexecuted log测试' % n)


@log01('executed')  # 给log函数传入字符串类型的参数'execute'，再给它传入函数类型的参数f()
def test2(n):
    print('这里是%sexecuted log测试' % n)


# 结果检验
test1('无')
test2('有')