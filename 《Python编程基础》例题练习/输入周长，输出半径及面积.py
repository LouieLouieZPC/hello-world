import math                                 # 调用数学
Π=math.pi
Π=int(Π)                                    # 取Π的整数
C=input('输入该圆的周长：')
C=float(C)                                  # 转字符串为浮点数
r=C/2/Π
S=Π*r**2
print('该圆的半径为：',r,'该圆的面积为：',S)