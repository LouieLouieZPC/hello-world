# 法一：
import steak                 # import 模块
steak.make_steak(9,'salad') # 模块名前缀.函数()
'''
运行结果如下：
Make a steak well done in 9 with the other:
———salad
'''
# 法一变种：指定模块别名
import steak as S          # import 模块 as 别名
S.make_steak(9,'red wine','salad')  # 模块别名前缀.函数()
'''
运行结果如下：
Make a steak well done in 9 with the other:
———red wine
———salad
'''
# 法二
from steak import make_steak()      # from 模块名 import 函数名
make_steak(9,'salad')               # 
