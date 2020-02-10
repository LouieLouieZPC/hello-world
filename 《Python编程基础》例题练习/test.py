import functools
def log01(text=None):   # 默认参数为None
    def decorator(func):  # 声明decorator装饰器
        @functools.wraps(func)
        def wrapper(*args, **kw):  # 第三层函数
            if text is not None:
                print('%s begin call %s()' % (text, func.__name__))
                fu = func(*args, **kw)      # 执行被装饰函数
                print('%s end call %s()' % (text, func.__name__))
            else:
                print('begin call %s()' % func.__name__)
                fu = func(*args, **kw)     # 执行被装饰函数
                print('end call %s()' % func.__name__)
            return fu

        return wrapper

    return decorator


@log01()  # 这种方法必须加(), 不能直接写@log01
def test1(n):
    print('这里是%sexecuted log测试' % n)


@log01('executed')  # 给log函数传入字符串类型的参数'execute'替代了原来的默认参数None
def test2(n):
    print('这里是%sexecuted log测试' % n)


# 结果检验
begin call test1()
这里是无executed log测试
end call test1()

executed begin call test2()
这里是有executed log测试
executed end call test2()