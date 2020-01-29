# 掌握嵌套函数————内建函数与外部函数
# 5.14 定义求均值函数
def mean(*args):           # 定义函数
    m=0
    def sum(x):            # 内建求和函数
        sum1=0             # 定义局部变量
        for i in x:
            sum1+=i
        return sum1        # 返回运算结果局部变量
    m=sum(args)/len(args)
    return m

'''
外部函数在返回结果时可直接调用内部函数的结果，以下!👇
'''
# 5.15 调用求均值函数
def mean(*args):          # 定义外部函数
    def sum(x):           # 定义内建函数
        sum1=0            # 定义局部变量
        for i in x:
            sum1+=i
        return sum1       # 返回内建函数运行结果（局部变量）
    return sum(args)/len(args)        # 直接返回sum函数的结果
z=[1,2,3,2]
print(mean(*z))
