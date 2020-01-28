#4.17 创建解析示例
# 例1，法一：
a=list(map(lambda x:x**3,range(6)))  # map函数根据提供的函数对指定序列做映射(lambda匿名函数 打印:程序段，一个或多个序列)
print(a)
# 例1，法二：
>>> [x**3 for x in range(6)]         # (打印 迭代)计算x的3次幂
[0, 1, 8, 27, 64, 125]

# 例2，法一：
seq=[1,2,3,4,5,6,7,8]
a=list(filter(lambda x:x%2,seq))     # filter用于过滤序列，过滤不符合条件的元素，返回符合条件元素组成新列表(lambda匿名函数 打印:条件，可迭代对象)
print(a)
# 例2，法二：
>>> seq=[1,2,3,4,5,6,7,8]
>>> [x for x in seq if x%2]          # (打印 迭代 满足的条件)当满足x%2有余数时打印出来
[1, 3, 5, 7]



#4.18 列表解析式嵌套循环示例
# 例1，法一：
>>> [(i,j) for i in range(0,3) for j in range(0,3)]    # (打印 迭代 嵌套迭代)
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 例1，法二：
for i in range(0,3):                                   # 法二与法一所得效果相同
    for j in range(0,3):
        print((i,j),end=',') 

# 例2，法一：
>>> [(i,j) for i in range(0,3) if i<1 for j in range(0,3) if j>1]   # (打印 迭代 满足的条件 嵌套迭代 满足的条件)
[(0, 2)]
# 例2，法二：
for i in range(0,3):                                                # 法二与法一所得效果相同
    if i<1:
        for j in range(0,3):
            if j>1:
                print([(i,j)])

