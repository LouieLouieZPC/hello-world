# 法一：
intCount=0
strCount=0
otherCount=0
element=input('请输入一段字符串：')   # 输入
for i in element:               # for循环语句
    if i.isdigit():
        intCount+=1
    elif i.isalpha():
        strCount+=1
    else:
        otherCount+=1
print(intCount,strCount,otherCount)    # 输出
