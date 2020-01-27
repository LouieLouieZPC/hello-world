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