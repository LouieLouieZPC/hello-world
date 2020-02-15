#-*-coding:utf-8-*-

for x in range(10,150000000000):                     # 迭代是10~15的数字
    for i in range(2,x):                   # 根据因子迭代
        if x%i==0:                         # 确定第一个因子
            j=x/i                          # 计算第二个因子
            print('%d等于%d*%d'%(x,i,j))   # %d表示格式化一个对象为字符；%表示转换说明符开始；在%左侧放一个要被格式化的字符串，右侧放希望格式化的值，()起来 
            break                          # 跳出当前if的循环
        else:
            print(x,'这是个质素')
            break                          # 跳出当前else的循环