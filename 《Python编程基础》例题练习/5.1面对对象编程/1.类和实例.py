'''
面对对象编程有两个关键内容：
1.类（class），例如：学生这一类
2.实例/对象（instance），例如：一个个具体的学生，小明、小红、小强
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。


属性：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
函数/方法：类中定义的函数。叫函数或者方法
self：代表类的实例，而非类，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
object：继承，表示该类是从哪个类继承下来的
'''

# 示例

class Cat：
    '一次模拟猫咪的简单测试'
    name='tesila'          # 属性，name变量是一个类变量，它的值将在这个类的所有实例之间共享。
    age=3                  # 属性，age变量是一个类变量，它的值将在这个类的所有实例之间共享。
    def sleep(self):       # 函数/方法
        '模拟猫咪被命令睡觉'
        print('%d岁的%s正在沙发上睡觉。'%(self.age,self.name))  # (调用函数方法，调用属性)
    def eat(self,food):    # 函数/方法
        '模拟猫咪被命令吃东西'
        self.food=food
        print('%d岁的%s在吃%s'%(self.age,self.name,self.food)) # (调用函数，调用属性，调用自定义函数)



# 一、创建/定义类（class）
'''
格式为：
class 类名(object)：  PS：类名是首字母大写或驼峰式命名的；object是继承的类
    '类的帮助信息'      # 类的帮助信息，类文档字符串
    属性列表
    方法/函数列表
'''
    class Student:
        pass

# 二、创建类的实例：
'''
格式为：
类名+()
'''

>>> bart = Student()                # 变量bart指向Student的实例
>>> bart
<__main__.Student object at 0x10a67a590>       # 后面的0x10a67a590是内存地址，每个object的地址都不一样
>>> Student
<class '__main__.Student'>          # 而Student本身则是一个类


# 三、给实例变量绑定属性：
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'


# 四、
class Student(object): 
    def __init__(self, name, score):  # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self
        self.name = name  # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
        self.score = score

# 五、传入参数
>>> bart = Student('Bart Simpson', 59)        # bart指向Student的实例，即self
>>> bart.name         # bart即类的实例self
'Bart Simpson'
>>> bart.score
59

# 六、self的名称可更改，不过最好按规定用self

class Test:
    def prt(my_address):
        print(my_adress)
        print(my_adress._class_)
t=Test()
t.prt()

# 查看类的属性和方法：用dir()函数
class Example:
    pass
example=Example()         # bart指向Student的实例/对象，即self,self即实例本身
dir(example)              # 用dir()函数，查看类的属性和方法，由于在定义里只有pass语句，所以结果都有下划线“_”开头结尾
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
  '__subclasshook__', '__weakref__']




