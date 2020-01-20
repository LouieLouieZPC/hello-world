# -*-coding:utf-8-*-
import math                                                                   # 调用数学
n1=float(input('请输入第一个数：'))                                             # 字符型转为数值型
n2=float(input('请输入第二个数：'))
n3=float(input('请输入第三个数：'))
m=3
x=(n1+n2+n3)/m                                                                # 除了双斜杠（//），只要任一操作为浮点数，其结果即为浮点数
y=((n1-x)**2+(n2-x)**2+(n3-x)**2)/m
z=int(math.sqrt(y))
print('计算得到的均值为：'+str(x)+'，方差为：'+str(y)+'，标准差约为：'+str(z))