def strnum(element):     # 定义一个函数，
    intCount=0
    strCount=0
    otherCount=0
    for i in element:
        if i.isdigit():
            intCount+=1
        elif i.isalpha():
            strCount+=1
        else:
            otherCount+=1
    return(intCount,strCount,otherCount)
element=input('请输入一段字符串：')
print(strnum(element))
