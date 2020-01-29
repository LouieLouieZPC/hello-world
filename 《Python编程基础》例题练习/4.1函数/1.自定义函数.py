#5.1 函数定义
>>> def my_function(parameter):        # del关键词（即definition） 函数名（形参）:
...  '打印任何传入的字符串'
...  print(parameter)
...  return 'parameter is '+parameter    # 返回函数值

# 5.2 默认参数
>>> def interest(money,day=1,interest_rate=0.05):      # 定义这么个函数,对以下整段程序逻辑封装
...  income=0
...  income=money*interest_rate*day/365
...  print(income)
# 5.3 默认参数使用
>>> interest(5000)               
0.684931506849315
>>> interest(money=5000)           # 关键字参数调用
0.684931506849315
>>> interest(10000)
1.36986301369863
# 5.4 任意数量的位置可变参数





