# -*-coding:utf-8-*-
# 正常方式
def add(a):            # 定义
    a+=3
    return a
x=[]
for i in range(10):
    x.append(add(i))   # 调用add函数，并append到list中
print(x)

# 用lambda函数方式 法一：
add=lambda a:a+3       # lambda可以作为对象赋值给变量
x=[]
for i in range(10):
    x.append(add(i))
print(x)
# 法二：
add=lambda a:a+3       # lambda可以作为对象赋值给变量
x=[]
[x.append(add(i)) for i in range(10)]     # 用列表解析高效创建列表
print(x)

# mad函数方式
numbers=list(range(10))                   # 用list和range函数快速创一个列表
x=list(map(lambda x:x+3,numbers))         # 用mad函数计算列表
print(x)
