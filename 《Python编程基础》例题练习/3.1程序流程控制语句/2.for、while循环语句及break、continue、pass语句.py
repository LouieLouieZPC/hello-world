'''
for是个秩序迭代器，用于遍历有序序列，包括字符串、列表、元组等
所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。
这两个语句通常都必须配合if语句使用。




'''
for target_list in expression_list:
    pass



#4.3 使用for循环对列表元素和字符串进行遍历,执行这段代码，会依次打印names的每一个元素：
>>> for i in['e','f','g']:           
...  print(i)
...
e
f
g
>>> for i in 'string':
...  print(i)
...
s
t
r
i
n
g

#4.4  while循环计数
>>> s=0
>>> while s<=1:
...  print('计数：',s)
...  s+=1
...
计数： 0
计数： 1


#4.5 无限次循环
>>> s=1
>>> while s<=1:
...  print('无限次循环')
无限次循环
无限次循环
无限次循环
无限次循环
.
.
.


#4.6 range函数的使用
>>> for i in range(0,5):
...  print(i)
...
0
1
2
3
4
>>> for i in range(0,6,2):          # 使用for i in range(start,stop,step):
...  print(i)
...
0
2
4
# 直接使用for循环难以改变序列元素
>>> L=[1,2,3]
>>> for i in L:                     # i不是引用、L对应的元素没有发生变化
...  i+=1
...  print(L)
...
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
>>> L=[1,2,3]
>>> for i in range(len(L)):         # for i in range(len(L)):来迭代整个列表L元素的索引，并通过索引修改
...  L[i]+=1                        # 通过索引修改
...  print(L)
...
[2, 2, 3]
[2, 3, 3]
[2, 3, 4]


#4.7 break语句的使用
>>> s=0
>>> while True:
...  s+=1
...  if s==6:                      # 满足s等于6时跳出循环
...   break
...
>>> s
6
>>> for i in range(0,10):
...  print(i)                      # 先执行输出，后面解释
...  if i==1:                      # 当i等于1时跳出循环
...   break                        # 跳过整个循环，包括从第一句到最后一句
...
0
1
>>> for i in range(0,10):
...  if i==1:
...   break
...  print(i)                      # 和上面不同的是这是后执行print(i)，当i等于1事终止了没有输出1
...
0
>>> for i in range(0,10):          
...  if i==1:                      # 干脆没有输出print(i)
...   break                        
...
>>>
>>>
>>>



# 4.8 continue语句的使用
>>> s=3                          # 定义变量
>>> while s>0:                   # while循环语句
...  s-=1
...  if s==1:                    # 当s等于1时跳出该次循环，执行下一个循环,若符合条件,continue会跳过当前循环的剩余语句，即print(s)
...   continue
...  print(s)                    
...
2
0
>>> for i in range(0,3):
...  if i==1:                    # 当i等于1时跳出本次循环
...   continue                    
...  print(i)
...
0
2


# 4.9 pass语句的使用
>>> for i in range(0,3):
...  if i==1:
...   pass                  # 用于在输出结果0~1之间占位，不做任何事情
...   print('pass块')          
...  print(i)
...
0
pass块
1
2


# Task
#-*-coding:utf-8-*-
# 连加 法一：
vec=[1,2,3,4,5,6,7,8,9,10]
m=0
for i in vec:
    m=m+i
    print(m)
...
1
3
6
10
15
21
28
36
45
55

# 法二：与法一的区别在于法一的输出在程序段中，经历了十次输出；法二的输出与for循环同级，循环完后再输出
vec=[1,2,3,4,5,6,7,8,9,10]
m=0
for i in vec:
    m=m+i
print(m)
55


# 连乘
vec=[1,2,3,4,5,6,7,8,9,10]
m=1
for i in vec:
    m=m*i
print(m)
