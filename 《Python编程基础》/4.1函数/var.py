# -*-coding:utf-8-*-

# 构建方差函数示例
'''
从全局角度看，主体方差函数下有1、2共两个子内建函数，
内建函数2下有一个子内建函数3
'''
def var(*args):                                     # 主体方差函数
    def sums(x):                                    # 内建函数1(不仅是x，可以用任意名字命名的位置参数)
        sum1=0                                  # 定义局部变量1
        for i in range(len(args)):
            sum1+=args[i]**2
        return sum1                             # 返回局部变量1
    def mean(y):                                    # 内建函数2
        def sum(z):                                 # 内建函数3
            sum2=0                              # 定义局部变量2
            for i in range(len(args)):
                sum2+=args[i]
            return sum2                         # 返回局部变量2
        return sum(args)/len(args)              # 返回mean函数的结果
    return sums(args)/len(args)-mean(args)**2   # 返回sums函数及mean函数的结果并计算方差