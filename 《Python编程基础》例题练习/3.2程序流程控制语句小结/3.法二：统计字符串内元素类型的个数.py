# 法二
'''
使用自定义函数：
语法：
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]

规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''



def strnum(element):     # 自定义一个函数，
    intCount=0
    strCount=0
    otherCount=0
    for i in element:    # for循环语句
        if i.isdigit():
            intCount+=1
        elif i.isalpha():
            strCount+=1
        else:
            otherCount+=1
    return[intCount,strCount,otherCount]
element=input('请输入一段字符串：')
print(strnum(element))                   # 调用函数