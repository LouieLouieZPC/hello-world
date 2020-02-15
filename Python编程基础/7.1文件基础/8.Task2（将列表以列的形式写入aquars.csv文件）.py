import csv
squares=[value**2 for value in range(1,101)]
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\\6.1文件基础\squares.py'
with open(file_name,'w',newline='') as f:          # newline=''选择空行
    x=csv.writer(f)
    for i in squares:
        x.writerow([str(i)])    # 转换成列表中的字符串，每行输出一个列表