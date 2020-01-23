 '''
创建字典：
    1.dict={key_1:value_1,key_2:value_2,...,key_n:value_n}
    2.转换列表对象为字典（双值子序列）：     变量名=dict([(key1,value1),(key2,value2),...,(keyn,value2)])
    3.变量名=dict（key1=value1,key2=value2,...,keyn=valuen）

测试是否存在（不会抽离原键与值）：
    1.key in 字典名
    2.字典名.get(key,代替值)

提取字典元素（提取值，不会抽离原键与值）：
    1.字典名[key]

增加字典元素：
    1.添加单个元素：                    字典名[key]=value
    2.添加多个元素/合并两个字典：        字典名1.update(字典名2)

删除字典元素：
    1.删除单个原键与值：                 del 字典名[key]
    2.会抽离原键与值：                  字典名.pop(key)/变量名=字典名.pop(key)
    3.删除所有元素：                    字典名.clear()

修改字典元素：
    1.变量名[key]=value

获取字典元素信息（所有键、所有值、所有键值对）（但不会抽离原键、值、键值对）：
    1.获取所有键：                      字典名.keys()
    2.获取所有值：                      字典名.values()
    3.获取所有键值对：                  字典名.itmes()

'''
 
 
 
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
#3.37
    >>> 'Canada' in country                       
    False
    >>> all_keys=country.keys()                   # 使用keys函数获取全部键
    >>> all_keys
    dict_keys(['China', 'America', 'Britain', 'French', 'Australia', 'Japan'])
    >>> all_values=country.values()               # 使用values函数获取全部值
    >>> all_values
    dict_values(['Beijing', 'Washington', 'London', 'Paris', 'Canberra', 'tokyo'])
    >>> 'Baijing' in all_values
    False
    >>> 'Beijing' in all_values                   # 判断字典是否包含此值
    True
    >>> list(all_values)                          # 将值的迭代形式转化为列表形式
    ['Beijing', 'Washington', 'London', 'Paris', 'Canberra', 'tokyo']
    >>> all_items=country.items()                 # 使用items函数得到全部键值对
    >>> all_items
    dict_items([('China', 'Beijing'), ('America', 'Washington'), ('Britain', 'London'), ('French', 'Paris'), ('Australia', 'Canberra'), ('Japan', 'tokyo')])
    >>> ('America','Washington') in all_items     # 判断字典是否包含此键值对
    True
    >>> all_items
    dict_items([('China', 'Beijing'), ('America', 'Washington'), ('Britain', 'London'), ('French', 'Paris'), ('Australia', 'Canberra'), ('Japan', 'tokyo')])
    >>> list(all_items)                           # 将键值对的迭代形式转换为列表形式
    [('China', 'Beijing'), ('America', 'Washington'), ('Britain', 'London'), ('French', 'Paris'), ('Australia', 'Canberra'), ('Japan', 'tokyo')]


#3.38
    >>> test={'A':100,'B':300,'C':True,'D':200}   
    >>> keys=list(test.keys())                    # ①使用key函数得到全部键②使用list函数将键的迭代形式转换为列表形式
    >>> values=list(test.values())                # 同上
    >>> keys
    ['A', 'B', 'C', 'D']
    >>> values
    [100, 300, True, 200]
    >>> keys[values.index(True)]                  # 故可利用值True的索引index来提取对应的键
    'C'


#Task：
# 法一：
    >>> # -*-coding:utf-8-*-

    >>> dict1={'Math':96,'English':86,'Chinese':95.5,'Biology':86,'Physics':None}      
    >>> dict1['History']=88                               # 增添键值对
    >>> del dict1['Physics']                              # 删除键值对
    >>> dict1['Chinese']=int(round(dict1['Chinese']))     # 将值进行四舍五入取整
    >>> dict1['Math']                                     # 查看键的对应值
    96
    >>> dict1                                             # 查看处理后的字典
    {'Math': 96, 'English': 86, 'Chinese': 96, 'Biology': 86, 'History': 88}
# 法二：
    >>> dict1=dict([('Math',96),('English',86),('Chinese',95.5),('Biology',86),('Physics',None)])
    >>> dict1
    {'Math': 96, 'English': 86, 'Chinese': 95.5, 'Biology': 86, 'Physics': None}
    >>> dict2=dict(History=88)        # 增加键值对
    >>> dict1
    {'Math': 96, 'English': 86, 'Chinese': 95.5, 'Biology': 86, 'Physics': None}
    >>> dict1.update(dict2)           # 增加键值对
    >>> dict1
    {'Math': 96, 'English': 86, 'Chinese': 95.5, 'Biology': 86, 'Physics': None, 'History': 88}
    >>> x=dict1.pop('Physics')        # 删除键值对，抽离此键与值
    >>> x
    >>> dict1
    {'Math': 96, 'English': 86, 'Chinese': 95.5, 'Biology': 86, 'History': 88}
    >>> dict1['Chinese']=int(round(dict1['Chinese']))        # 将值四舍五入后取整
    >>> dict1
    {'Math': 96, 'English': 86, 'Chinese': 96, 'Biology': 86, 'History': 88}
    >>> dict1['Math']                                        # 查看键的对应值
    96