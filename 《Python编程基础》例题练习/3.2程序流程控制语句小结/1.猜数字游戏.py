#-*-coding:utf-8-*-

import random
x=random.randint(0,500)
print('《猜数字游戏》')
num=int(input('电脑已随机生成一个0~500的整数，请输入一个数字看看是否与电脑给的一样:'))
guess=1
while num!=x:
    while type(num)==<class 'int'>:
        if num>x:
            print('你第%d次输入的数字比电脑的随机数字大'%num)
            num=input('请再次输入数字：')
            guess+=1
        elif num<x:
            print('你第%d次输入的数字比电脑的随机数字小'%num)
            num=input('请再次输入数字：')
            guess+=1



    else:
        print('您所输入的不符合规范，请重新输入！')
        num=input('请重新输入符合规范的数字：')
        continue
else:
    print('恭喜您，您第%d次输入的数字%d与电脑的随机数字%d一样'%(guess,num,x))