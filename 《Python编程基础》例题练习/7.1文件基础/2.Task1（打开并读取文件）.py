txts=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\Walden.txt'
with open(txts,'r',encoding='UTF-8') as f:          # 再加一个编码方式encoding='UTF-8'
    x=f.read()
print(x)