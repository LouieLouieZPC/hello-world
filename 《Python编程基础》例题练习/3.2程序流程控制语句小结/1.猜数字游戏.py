#-*-coding:utf-8-*-

import random
x=random.randint(0,500)
print('《猜数字游戏》')
num=int(input('电脑已随机生成一个0~500的整数，请输入一个数字看看是否与电脑给的一样:'))
guess=0
while type(num) is int:
    while num!=x:
        if num>x:   
            guess+=1
            print('你第%d次输入的数字%d比电脑的随机数字大'%(guess,num))
            num=input('请再次输入数字：')
        elif num<x:         
            guess+=1
            print('你第%d次输入的数字%d比电脑的随机数字小'%(guess,num))
            num=input('请再次输入数字：')
        break
    else:
        guess+=1
        print('恭喜您，您第%d次输入的数字%d与电脑的随机数字%d一样'%(guess,num,x))
else:
    print('您所输入的不符合规范，请重新输入！')
    num=int(input('请重新输入符合规范的数字：'))