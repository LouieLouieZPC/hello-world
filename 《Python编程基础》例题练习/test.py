from functools import wraps
def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2020.2.10')

now()