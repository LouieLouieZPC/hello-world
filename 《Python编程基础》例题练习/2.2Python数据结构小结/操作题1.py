#-*-coding:utf-8-*-


list1=[5,8,-7,4,6,2,-3,0]
print('列表的最大元素为：',max(list1))
x=min(list1)
print(x)
y=list1.index(x)
del list1[y]
list1[5]=abs(list1[5])
print('最后结果为：',list1)