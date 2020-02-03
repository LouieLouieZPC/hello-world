# 7.22 写入文件
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\word.txt'
with open(file_name,'w') as f:
    f.write('hello,world!\n')
    f.write('i love python!\n')

# 7.24 对文件添加内容
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\word.txt'
with open(file_name,'a') as f:
    f.write('what\'s your favorite language?\n')
    f.write('my favorite language is python too!\n')
