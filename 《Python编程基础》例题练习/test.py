try:
    x=int(input('请输入计划代码:'))
    print('正在执行代码：%s'%x)
except ValueError:
    print('您输入的代码有误！')
else:
    print('**************************')
    print('没有异常,正在执行下一段代码')
finally:
    print('**************************')
    print('有无异常都必然执行的代码')