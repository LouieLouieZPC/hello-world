set1={1,2,3,4,6,8,12,24}
set2={1,2,3,4,6,9,12,18,36}
x=max(set1|set2)
y=max(set1&set2)
z=set1-set2
n=set1-set2
m=set2-set1
print('24的最大公约数为：',x)
print('36的最小公倍数为：',y)
print('24独有的约数集合为：',n)
print('36独有的约数集合为：',m)