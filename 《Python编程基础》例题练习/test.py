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
 
for x in myclass:
  print(x)