>>> L=[1,2,3]
>>> it=iter(L)
>>> it
<list_iterator object at 0x0000023B1BCEFFD0>
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration