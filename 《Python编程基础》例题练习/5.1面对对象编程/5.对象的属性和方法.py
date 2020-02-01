# 6.7创建实例
class Cat():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sleep(self):
        print('%d岁的%s正在沙发上睡懒觉。'%(self.age,self.name))
    def eat(self,food):
        self.food=food
        print('%d岁的%s正在吃%s。'%(self.age,self.name,self.food))
cat1=Cat('Tom',3)                 # 创建实例/对象cat1需要参数
cat2=Cat('Jack',4)                # 创建实例/对象cat1需要参数
print('Cat1的名字为：',cat1.name)  # 调用函数
print('Cat2的名字为：',cat2.name)  # 调用函数
print(cat1.sleep())               # 访问对象的方法/函数sleep，记得加括号
print(cat2.eat('fish'))           # 访问对象的方法/函数eat，记得加括号

'''
上述结果如下：
Cat1的名字为： Tom
Cat2的名字为： Jack
3岁的Tom正在沙发上睡懒觉。
None
4岁的Jack正在吃fish。
None
'''


# 6.8对象方法的引进
cat1=Cat('Tom',3)
sleep=cat1.sleep      # 对象的方法/函数sleep的引用
print(sleep())        # 记得加括号

cat1=Cat('Tom',3)
eat=cat1.eat     # 对象的方法/函数eat的引用
print(eat())     # 记得加括号

