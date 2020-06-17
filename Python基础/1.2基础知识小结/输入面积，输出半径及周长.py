# 输入圆的半径，输出面积周长

import math                        # 调用数学
Π=math.pi                          # 定义Π
Π=int(Π)                           # 对Π取整数
S=input('输入该圆面积：')           # 输入该圆的面积
S=float(S)                         # 将字符串转换为浮点数
r=math.sqrt(S/Π)                   # 用Python数字sqrt()函数开平方
C=math.sqrt(4*S*Π)
print('该圆半径为：',r,'该圆周长为：',C)   #  输出该圆的半径和该圆的周长