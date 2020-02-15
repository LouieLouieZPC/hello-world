def midnum(*args):
    args=list(args)
    args.sort()
    if len(args)%2==1:
        n1=len(args)//2
        return('该列表元素个数为奇数，中位数为：',args[n1])
    elif len(args)%2==0:
        n2=(len(args)//2)-1
        m=n2+1
        z=(args[n2]+args[m])/2
        return('该列表元素个数为偶数，中位数为：',z)
args=[3,1,4,2]
print(midnum(*args))