# filter function

**语法：**  
filter(function, iterable)  (起'筛选'作用)(常搭配list()函数使用)  
* function -- 判断函数。
* iterable -- 可迭代对象。  
* 返回一个迭代器对象

和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素

**注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list**


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