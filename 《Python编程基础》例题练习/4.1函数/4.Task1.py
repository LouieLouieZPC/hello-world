# -*-coding:utf-8-*-

# 构建方差函数示例

def var(*args):
    def sums(x):
        sum1=0
        for i in range(len(args)):
            sum1+=args[i]**2
        return sum1
    def mean(y):
        def sum(z):
            sum2=0
            for i in range(len(args)):
                sum2+=args[i]
            return sum2
        return sum(args)/len(args)
    return sums(args)/len(args)-mean(args)**2
args=[1,2,3,4]
print(var(*args))
        
            
