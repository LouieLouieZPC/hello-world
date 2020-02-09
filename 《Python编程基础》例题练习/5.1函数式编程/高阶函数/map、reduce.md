# map function and reduce function

## 一、map function

**语法：**  
map(function, iterable, ...)  (常搭配list()函数使用)  
function -- 函数  
iterable -- 可迭代对象  
`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`(迭代器)返回

由于结果是一个`Iterator`，Iterator是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个`list`

**e.g.:**
```python
def f(x):
    return x*x
print(list(map(f,range(1,10))))
```
map()作为高阶函数,可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

```python
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```


***************************
## 二、reduce function

**语法：**  

reduce(function, iterable[, initializer])  

function -- 函数，有两个参数  
iterable -- 可迭代对象  
initializer -- 可选，初始参数  