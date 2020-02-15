#-*-coding:utf-8-*-

# 完整金字塔
num=eval(input('请输入一个整数：'))
print('数字金字塔显示如下：')
level=1   # 金字塔的高度即层数
while level<=num:
    kk=1    # 每一层长度计数
    t=level
    length=2*t-1
    while kk<=length:
        if kk==1:
            if kk==length:
                print(format(t,str(2*num-1)+'d'),'\n')
                break
            else:
                print(format(t,str(2*num+1-2*level)+'d'),'',end='')
                t-=1
        else:
            if kk==length:
                print(t,'\n')
                break
            elif kk<=length/2:
                print(t,'',end='')
                t-=1
            else:
                print(t,'',end='')
                t+=1
        kk+=1
    level+=1
                