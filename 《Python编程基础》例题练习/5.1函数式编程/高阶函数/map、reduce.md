# map function and reduce function

## 一、map function

**语法：**  
map(function, iterable, ...)  (常搭配list()函数使用)  
function -- 函数  
iterable -- 可迭代对象  
`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`(迭代器)返回



**e.g.1:**  
由于结果是一个`Iterator`，Iterator是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个`list`:
```python
def f(x):
    return x*x
print(list(map(f,range(1,10))))
```

**e.g.2:**  
map()作为高阶函数,可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

```python
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```


**********************************************************
## 二、reduce function

**语法：**  

reduce(function, iterable[, initializer])  

function -- 函数，有两个参数  
iterable -- 可迭代对象  
initializer -- 可选，初始参数  

**e.g.1:**  
用`reduce()`实现求和，同`sum()`效果：

```python
>>> from functools import reduce
>>> r=reduce(lambda x,y:x+y,[1,2,3,4,5])
>>> print(r)
15
```


**e.g.2:**  
把序列`[1, 3, 5, 7, 9]`变换成整数`13579`：

```python
>>> from functools import reduce
>>> def fn(x,y):
        return x*10+y
>>> n=reduce(fn,[1,3,5,7,9])
>>> print(n)
13579
```

**e.g.3:**  
造一个把str转换为int的函数：

```python
>>> from functools import reduce
>>> DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

>>> def char2num(s):
>>>     return DIGITS[s]

>>> def str2int(s):
>>>     return reduce(lambda x, y: x * 10 + y, map(char2num, s))  # s这个位置参数放字符串
>>> print(str2int('12345'))
12345
```