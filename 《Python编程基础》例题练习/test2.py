class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self         # __iter__() 方法返回一个特殊的迭代器对象
 
  def __next__(self):
    x = self.a
    self.a += 1         # 初始值为 1，逐步递增 1
    return x
 
myclass = MyNumbers()   # 创建类的对象
for i in myclass:
    print(i)
