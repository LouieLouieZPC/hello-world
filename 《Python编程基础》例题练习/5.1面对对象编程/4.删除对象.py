class Animal():
    def _init_(self):
        print('---构造方法被调用---')
    def _del_(self):
        print('---解析方法被调用---')
cat=Animal()                                   # 每当根据类创建新实例/对象时，默认自动调用构造方法，python都会自动运行_init_，
print(cat)
<__main__.Animal object at 0x00000269CC6D6AC0>
del cat                                        # 当删除一个对象时，同样会默认调用解析方法
print(cat)
Traceback (most recent call last):
  File "d:/01.Software/GitHub/GitHub Repository/hello-world/《Python编程基础》例题练习/5.1面对对象编程/4.删除对象.py", line 9, in <module>
    print(cat)
NameError: name 'cat' is not defined