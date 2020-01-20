import math                               # 调用数学
Π=math.pi                                 # 定义Π
r=input('输入该圆半径：')
r=float(r)                                # input（）函数输入的是字符串格式；转换为浮点数
C=2*Π*r
S=Π*r**2
print('该圆面积为：',S,'该圆周长为：',C,)