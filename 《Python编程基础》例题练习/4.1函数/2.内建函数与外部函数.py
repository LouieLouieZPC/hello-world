# 掌握嵌套函数————内建函数与外部函数
# 5.14 定义求均值函数
def mean(*args):           # 定义函数
    m=0
    def sum(x):            # 内建求和函数
        sum1=0
        for i in x:
            sum1+=i
        return sum1
    m=sum(args)/len(args)
    return m

# 5.15 调用求均值函数
def mean(*args):
    def sum(x):
        sum1=0