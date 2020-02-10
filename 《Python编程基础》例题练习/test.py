def now():
    print('2020.2.10')
f=now     # 函数也是个对象，函数对象被赋值给变量
f()       # 调用该函数

print(now.__name__)   
print(f.__name__)    # __name__属性，拿到函数的名字



f = abs
print(f)



from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
 
@decorator_name
def func():
    return("Function is running")

can_run = False
print(func())
# Output: Function will not run