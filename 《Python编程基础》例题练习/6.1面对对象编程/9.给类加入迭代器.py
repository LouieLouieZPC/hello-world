# 9.给类加入迭代器
'''
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
'''
# 例一、
class  Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.info=[self.name,self.age]
        self.index=-1         # 为迭代设置初始变量
    def getName(self):        # 函数：通过设置好的接口函数来访问对象
        return self.name
    def getAge(self):         # 函数：通过设置好的接口函数来访问对象
        return self.age
    def _iter_(self):         # 加入迭代器
        print('名字 年龄')
        return self           # __iter__() 方法返回一个特殊的迭代器对象
    def next(self):
        if self.index==len(self.info)-1:
            raise StopAsyncIteration
        self.index+=1
        return self.info[self.index]
newcat=Cat('coffe',3)         # 创建类的对象
print(newcat.getName())       # 通过设置好的接口函数来访问对象的属性
'''
结果如下：
coffe
'''
iterator=iter(newcat.next,1) # 创建迭代器对象，变量=iter(类的对象)，调用迭代函数来输出对象的属性
for info in iterator:
    print(info)
'''
结果如下：
coffe
3
'''



# 例二、
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self         # __iter__() 方法返回一个特殊的迭代器对象
 
  def __next__(self):
    x = self.a
    self.a += 1         # 初始值为 1，逐步递增 1
    return x
 
myclass = MyNumbers()   # 创建类的对象
myiter = iter(myclass)  # 创建迭代器对象，变量=iter(类的对象)

print(next(myiter))     # 输出迭代器的下一个元素，next()
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
以上结果如下：
>>> print(next(myiter))
1
>>> print(next(myiter))
2
>>> print(next(myiter))
3
>>> print(next(myiter))
4
>>> print(next(myiter))
5
'''


# 例三、
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration    # 在 20 次迭代后停止执行
 
myclass = MyNumbers()        # 创建类的对象
myiter = iter(myclass)       # 创建迭代器对象，变量=iter(类的对象)
 
for x in myiter:
  print(x,end=',')

'''
以上结果如下：
1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
'''