#-*-coding:utf-8-*-

mppx=[1,8,2,6,3,9,4,12,0,56,45]                # 定义列表
for i in range(len(mppx)):                     # 迭代整个列表mpxx的元素索引
    for j in range(i+1):                       # 遍历
        if mppx[i]<mppx[j]:                    # 通过索引访问比较大小
            mppx[i],mppx[j]=mppx[j],mppx[i]    # 元素位置呼唤
print(mppx)                                    # 结果和使用mppx.sort函数所得升序排序效果相同