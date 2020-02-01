# 6.13 迭代器（iteration）的两个基本函数：iter函数与next函数
>>> L=[1,2,3]         # 字符串，列表或元组对象都可用于创建迭代器
>>> it=iter(L)        # 调用iter函数创建迭代器对象，变量=iter()
>>> it             
<list_iterator object at 0x0000023B1BCEFFD0>
>>> next(it)          # 输出迭代器的下一个元素，next()
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)         #容器对象遍历/迭代完毕，next函数找不到后续元素引发StopIteration异常，告知for循环终止
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration        # 停止迭代


# 迭代器对象可以使用常规for语句进行遍历、
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")
'''
结果如下：
1 2 3 4
'''