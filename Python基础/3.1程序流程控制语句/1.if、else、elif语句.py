#-*-coding:utf-8-*-

score=float(input('输入本次考试成绩:'))
if score>=90 and score<=100:
    print('本次考试，成绩等级为：A')
elif score>=80 and score<90:
    print('本次考试，成绩等级为：B')
elif score>=70 and score<80:
    print('本次考试，成绩等级为：C')
elif score>=60 and score<70:
    print('本次考试，成绩等级为：D')
else:
    print('本次考试，成绩等级为：E')


# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。


# if判断条件还可以简写，比如写：
if x:
    print('True')
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。