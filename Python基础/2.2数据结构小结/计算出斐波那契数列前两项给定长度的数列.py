#-*-coding:utf-8-*-
# 计算出斐波那契数列前两项给定长度的数列

F1=0
F2=1
list1=[F1,F2]
F3=F1+F2;list1.append(F3)
F4=F2+F3;list1.append(F4)
F5=F3+F4;list1.append(F5)
F6=F4+F5;list1.append(F6)
list1.pop(2)
print('此指定长度为5的数列为：',list1)
F6=sum(list1)
print('此时数列各项之和为:',F6)
list1.append(F6)
print('追加新项的数列为：',list1)