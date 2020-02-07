 '''

有序、不可变

创建元组：
    1.变量名=()    只有1个元素的tuple定义时必须加一个逗号,
    2.变量名=tuple()

元组索引提取（不会变更原元素）：
    1.元组名[index]

元组切片提取（左闭右开）：
    1.元组名[start:stop:step]

元组解包（类似贴标签）：
    1.变量名1,变量名2,...,变量名n=元组名/
      变量名1,变量名2,...,变量名n=元素1,元素2,...,元素n

查询元组元素位置：
    1.元组名.index(index)



    
'''


#3.20
    >>> mytuple1=(1,2.5,('three','four'),[True,5],False)         # 使用圆括号()创建元组
    >>> mytuple1
    (1, 2.5, ('three', 'four'), [True, 5], False)
    >>> mytuple2=2,True,'five',3.5                               # 省略圆括号()创建元组 
    >>> mytuple2    
    (2, True, 'five', 3.5)                                       # 结果会自动补上圆括号
    >>> empty_tuple=()                                           # 创建空元组
    >>> empty_tuple
    ()

#3.21
    >>> mytuple1=tuple([1,2.5,('three','four'),[True,5],False])  # 使用tuple函数将列表转换为元组
    >>> mytuple1
    (1, 2.5, ('three', 'four'), [True, 5], False)    
    >>> mytuple2=tuple((2,True,'five',3.5))                      # 使用tuple函数将元组转换为元组
    >>> mytuple2
    (2, True, 'five', 3.5)
    >>> empty_tuple=tuple()                                      # 使用tuple函数创建空元组
    >>> empty_tuple
    ()


#3.22
    >>> mytuple3=('China','America','England','France')          
    >>> mytuple3[0]                                              # 提取元组第一个元素
    'China'
    >>> mytuple3[10]                                             # 传入的索引超出元组索引范围
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: tuple index out of range                         # 传入的索引超出元组索引范围
#3.23
    >>> mytuple3[-2::-1]                                         # 提取元素倒数第2个元素到左端之间所有元素
    ('England', 'America', 'China')
    >>> mytuple3[1:10]                                           # 超出元素索引范围
    ('America', 'England', 'France')                            
#3.24
    >>> A,B,C,D=mytuple3                                         # 将元组中的各元素分别赋值给对应变量（贴标签）
    >>> A
    'China'
    >>> B
    'America'
    >>> C
    'England'
    >>>
    >>> D
    'France'
    >>> X,Y,Z=1,True,'one'                                       # 利用元组解包进行多个变量赋值（元组可省略圆括号）
    >>> X
    1
    >>> Y
    True
    >>> Z
    'one'
    >>> X,Y,Z=1
    Traceback (most recent call last):  
    File "<stdin>", line 1, in <module>
    TypeError: cannot unpack non-iterable int object

#3.25
    >>> mytuple4=('A','D','C','A','C','B','B','A')              
    >>> mytuple4.count('b')                                     # 使用count函数进行元素计数
    0
    >>> mytuple4.count('B')                                     # 使用count函数进行元素计数
    2
    >>> mytuple4.index('C')                                     # 使用index函数获取元素在元组第一次出现的位置索引
    2
    >>> sorted(mytuple4)                                        # 使用sorted函数对元组元素进行排序，默认为升序
    ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D']
    >>> len(mytuple4)                                           # 使用len函数获取元组长度
    8
    >>> (1,2,3)+(4,5,6)                                         # 使用元组加法合并两个元组  
    (1, 2, 3, 4, 5, 6)
    >>> (10,20,30,40,50)*3                                      # 使用元组乘法重复合并元组
    (10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

#3.1 task
    >>> list=['pen','paper',10,False,2.5]                       # 定义list函数
    >>> type(list)                                              # 查询对象的数据类型
    <class 'list'>
    >>> list=tuple(list)                                        # 转换列表对象为元组类型
    >>> type(list)                                              # 查询对象的数据类型
    <class 'tuple'>
    >>> list.index(False)                                       # 查询元素位置索引
    3
    >>> element=list[3]                                         # 提取元组元素
    >>> print(element)                                          # 查看元组元素
    False
    