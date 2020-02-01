# 6.13 迭代器（iteration）的两个基本函数：it函数与next函数
>>> L=[1,2,3]
>>> it=iter(L)        # 调用iter函数
>>> it             
<list_iterator object at 0x0000023B1BCEFFD0>
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)         #容器对象遍历/迭代完毕，next函数找不到后续元素引发StopIteration异常，告知for循环终止
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration        # 停止迭代

# 