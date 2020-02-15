# -*-coding:utf-8-*-

import var                         # 导入封装好的函数模块var
var1=var.var(1,3,5,7,9,11,13)
print(var1)

import var as v                    # 给函数模块指定别名v
vart2=V.var(8,9,10,11)
print(var2)

from var import var                # 导入模块中的函数var.var
var3=var(5,6,7,8,9)
print(var3)

from var import var as fangcha     # 给函数指定别名fangcha
var4=fangcha(5,6,7,8,9)
print(var4)

from var import *                  # 导入模块中所有的函数