 #3.26
    >>> mydict1={'myint':1,'myfloat':3.1415,'mystr':'name','myint':100,'mytuple':(1,2,3),'mydict':{}}    # 使用花括号创建字典
    >>> mydict1
    {'myint': 100, 'myfloat': 3.1415, 'mystr': 'name', 'mytuple': (1, 2, 3), 'mydict': {}}               # 对于重复的键，键会采用最后出现的对应值
    >>> empty_dict=()                                                                                    # 创建一个空字典                  
    >>> empty_dict 
    ()

#3.27
    >>> mydict1=dict([('myint',1),('myfloat',3.1415),('mystr','name'),('myint',100),('mytuple',(1,2,3)),('mydict',{})])    # 法一：使用dict函数转换列表对象（双值子序列）为字典
    >>> mydict1
    {'myint': 100, 'myfloat': 3.1415, 'mystr': 'name', 'mytuple': (1, 2, 3), 'mydict': {}}
    >>> mydict2=dict(zero=0,one=1,two=2)                   # 法二：直接向dict
    >>> mydict2
    {'zero': 0, 'one': 1, 'two': 2}
    >>> empty_dict=dict()
    >>> empty_dict
    {}


#3.28
    >>> mydict3={'spring':(3,4,5),'summer':(6,7,8),'autumn':(9,10,11),'winter':(12,1,2)}    # 创建一个字典，内部为字符的键和元组的值
    >>> mydict3['autumn']                     # 提取键为'autumn'的对应值
    (9, 10, 11)
    >>> mydict3['Spring']                     # 提取字典中不存在的键'Spring'所对应的值
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    KeyError: 'Spring'                        # 提示：键错误
#3.29
    >>> 'spring' in mydict3                   # 用in语句检查传入的键是否存在
    True
#3.30
    >>> mydict3.get('summer')                 # 用字典方法get传入存在的键并返回对应值（只传键不传代替值）
    (6, 7, 8)
    >>> mydict3.get('Spring')                 # 用字典方法get传入不存在的键，只会不返回任何东西（只传键不传代替值）
    >>> print(mydict3.get('Spring'))          # 打印函数返回的结果
    None
    >>> mydict3.get('Spring','Not in this dict')  # 用字典方法get传入不存在的键，会返回代替值（既传键又传代替值）
    'Not in this dict'
    >>> mydict3.get('spring','in this dict')      # 用字典方法get传入存在的键，会返回原本的对应值（既传键又传代替值）（因此代替值只是临时存在的）
    (3, 4, 5)


#3.31
    >>> country=dict(China='Beijing',America='Washington',Britain='London',French='Paris',Canada='Ottawa')    # 使用dict函数创建字符
    >>> country_copy=country.copy()               # 用copy创建一个副本字典对象
    >>> country_copy['Russian']='Moscow'          # 增添元素一个函数
    >>> country_copy                              # 查看字典
    {'China': 'Beijing', 'America': 'Washington', 'Britain': 'London', 'French': 'Paris', 'Canada': 'Ottawa', 'Russian': 'Moscow'}
#3.32
    >>> others=dict(Australia='Canberra',Japan='Tokyo',Canada='OTTAWA')      # 使用dict函数创建字典
    >>> country.update(others)                                               # 用字典方法update函数增添多个函数
    >>> country
    {'China': 'Beijing', 'America': 'Washington', 'Britain': 'London', 'French': 'Paris', 'Canada': 'OTTAWA', 'Australia': 'Canberra', 'Japan': 'Tokyo'}
#3.33
    >>> country_copy=country.copy()               # copy一个副本字典对象
    >>> del country_copy['Canada']                # 使用del函数删除副本字典中的元素
    >>> country_copy
    {'China': 'Beijing', 'America': 'Washington', 'Britain': 'London', 'French': 'Paris', 'Australia': 'Canberra', 'Japan': 'Tokyo'}
#3.34
    >>> old_value=country.pop('Canada')           # 用pop语句将键对应的值赋给变量，并删除键值对
    >>> old_value
    'OTTAWA'
    >>> country
    {'China': 'Beijing', 'America': 'Washington', 'Britain': 'London', 'French': 'Paris', 'Australia': 'Canberra', 'Japan': 'Tokyo'}
#3.35
    >>> country_copy=country.copy()               # copy字典副本
    >>> country_copy.clear()                      # 用clear清除副本字典内容
    >>> country_copy                              # 变成一个空值
    {}
#3.36
    >>> country['Japan']='tokyo'                  # 直接新值赋给对应元素
    >>> country
    {'China': 'Beijing', 'America': 'Washington', 'Britain': 'London', 'French': 'Paris', 'Australia': 'Canberra', 'Japan': 'tokyo'}
#3.7
