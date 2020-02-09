# filter function

**语法：**  
filter(function, iterable)  (起'筛选'作用)(常搭配list()函数使用)  
* function -- 判断函数。
* iterable -- 可迭代对象。  
* 返回一个迭代器对象

和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素

**注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list**


**e.g.1:**  
过滤出列表中的所有奇数：
```python
#!/usr/bin/python3
 
def is_odd(n):
    return n % 2 == 1
 
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)
```

**e.g.2:**  
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

```python
def is_palindrome(x):
    x=str(x)
    return x==x[::-1]

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
```