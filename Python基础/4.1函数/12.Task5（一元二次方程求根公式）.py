# -*-coding:utf-8-*-
import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) and not isinstance(b,(int,float)) and not isinstance(c,(int,float)):
        raise TypeError('输入数字！')
    if b**2-4*a*c<0:
        return('bad value: (b**2-4*a*c)<0',)
    else:
        x=math.sqrt(b**2-4*a*c)
        y=(-b+x)/2*a
        z=(-b-x)/2*a
        return('一个答案是：%d,另一个答案是：%d'%(y,z))

r=quadratic(2,3,1)
print(r)
