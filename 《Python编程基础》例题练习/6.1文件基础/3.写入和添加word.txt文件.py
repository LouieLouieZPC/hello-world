'''
写入文件：
'w'写文本文件（字符串格式）会新增文件，若重名会覆盖原文件（'wb'写二进制文件）（'rb'读二进制文件）
f.write
对文件添加内容：
'a'
f.write
'''



# 7.22 写入文件
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\word.txt' 
with open(file_name,'w') as f:       # 打开，'w'写文本文件（字符串格式）会新增文件，若重名会覆盖原文件（'wb'写二进制文件）（'rb'读二进制文件）
    f.write('hello,world!\n')        # write函数
    f.write('i love python!\n')      # write函数

# 7.24 对文件添加内容
file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\word.txt'
with open(file_name,'a') as f:       # 打开，'a'添加
    f.write('what\'s your favorite language?\n')    # write函数
    f.write('my favorite language is python too!\n')  # write函数
