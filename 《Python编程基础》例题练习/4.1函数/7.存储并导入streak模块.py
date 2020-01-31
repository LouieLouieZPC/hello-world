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
make_steak(9,'salad')               # 不需要加模块名前缀了，直接调用函数名称

# 法二变种：指定函数别名
from steak import make_steak as ms  # from 模块名 import 函数名 as 函数别名
ms(9,'salad')                       # 不需要加模块名前缀了，直接调用函数别名

# 法三：导入所有函数
from steak import *                 # 导入模块中所有函数，在编写大型程序时尽量少用
make_steak(9,'salad')               # 不需要加模块名前缀了，直接调用函数名称
