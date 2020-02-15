#-*-coding:utf-8-*-

count=0                   # 定义变量
while count<5:
    if count>3:           # 先执行if~else的程序段
        print(count**2)
    else:
        print(count)
    count=count+1         # 再执行下一句程序，依次执行
