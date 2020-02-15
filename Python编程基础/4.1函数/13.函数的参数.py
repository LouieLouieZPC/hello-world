'''
位置参数:
power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。
'''
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
power(5, 2)






'''
默认参数:
一是必选参数在前，默认参数在后，否则Python的解释器会报错
二是当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
注：定义默认参数要牢记一点：默认参数必须指向不可变对象(例：数字型数据，字符型数据、元组、不可变集合)！
'''
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
'''
解释：
有多个默认参数时，调用的时候，既可以按顺序提供默认参数，\
比如调用enroll('Bob', 'M', 7)，意思是，除了name，gender这两个参数外，最后1个参数应用在参数age上，city参数由于没有提供，仍然使用默认值。

也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。比如调用enroll('Adam', 'M', city='Tianjin')，
意思是，city参数用传进去的值，其他默认参数继续使用默认值。
'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L








'''
可变参数:
可变参数允许你传入0个或任意个参数，
这些可变参数在函数调用时自动组装为一个tuple。
'''

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

'''
定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数：
'''
>>> calc(1, 2)
5
>>> calc()
0
'''
Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''
>>> nums = [1, 2, 3]
>>> calc(*nums)
14









'''
关键字参数:
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


在调用该函数时，可以只传入必选参数：
>>> person('Michael', 30)
name: Michael age: 30 other: {}


也可以传入任意个数的关键字参数：
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}


也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去:
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
'''
**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
对kw的改动不会影响到函数外的extra。
'''







'''
命名(限制)关键字参数:
'''
'''
1.不允许特定参数进入：
'''
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

'''
2.只接收city和job作为关键字参数：
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
*后面的参数被视为命名关键字参数
'''
def person(name, age, *, city, job):
    print(name, age, city, job)


'''
3.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
'''
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
'''
命名关键字参数必须传入参数名,否则报错:
由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
'''






'''
参数组合:
1.参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)



'''
2.函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
'''
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}


'''
3.最神奇的是通过一个tuple和dict，你也可以调用上述函数：
对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}








'''
小结：
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''