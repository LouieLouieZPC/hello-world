'''
参数检查
调用函数时:
如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
如果参数类型不对，Python解释器就无法帮我们检查


数据类型检查可以用内置函数isinstance()实现
isinstance(object, classinfo)
object -- 实例对象。
classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。
如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
'''



def my_ads(x):
    if not isinstance(x,(int,float)):    #   对参数类型做检查，只允许整数和浮点数类型的参数
        raise TypeError('Bad operand type')    # 如果传入错误的参数类型，函数就可以抛出一个错误
    if x>=0:
        return x
    else:
        return -x
my_ads()