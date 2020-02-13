from enum import Enum,unique

@unique        # 若要不能定义相同的成员值，可以通过 unique 装饰,否则默认成员值可以相同  
class Weekday(Enum):
    Sun=0        # 成员名name=成员值value
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

day1=Weekday.Sun
print(day1)
print(day1==Weekday.Sun)
print(Weekday.Mon)
print(Weekday.Mon.value)
print(Weekday.Mon.name)
print(Weekday['Tue'])
print(Weekday(4))

for name,number in Weekday.__members__.items():
    print(name,'==>',number)


# Output:
Weekday.Sun
True
Weekday.Mon
1
Mon
Weekday.Tue
Weekday.Thu
Sun ==> Weekday.Sun
Mon ==> Weekday.Mon
Tue ==> Weekday.Tue
Wed ==> Weekday.Wed
Thu ==> Weekday.Thu
Fri ==> Weekday.Fri
Sat ==> Weekday.Sat
