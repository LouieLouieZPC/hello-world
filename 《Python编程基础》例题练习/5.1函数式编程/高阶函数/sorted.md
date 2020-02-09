# 排序算法

**sorted 语法：**  
sorted(iterable, key=None, reverse=False)  

* iterable -- 可迭代对象。  
* key -- (忽略效果)主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。  
* reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。




**e.g.1:**  
例如按绝对值大小排序：
> ```python
> >>> sorted([36, 5, -12, 9, -21], key=abs)
> [5, 9, -12, -21, 36]
>```


**e.g.2:**  
我们提出排序应该忽略大小写，按照字母序排序，并反向排序。只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较，传入第三个参数reverse=True。  


> ```python
> >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
> ['Zoo', 'Credit', 'bob', 'about']
> ```



**e.g.3:**  
对列表里的元组分别按名字排序：


> ```python
> L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
> L2 = sorted(L, key=lambda L:L[0])    # key是对list里的元素来说的,key=lambda L:L[0]中的L其实是('Bob', 75)
> print(L2)
> [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
> ```
