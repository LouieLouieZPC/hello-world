txts=r'D:\01.Software\GitHub\GitHub Repository\hello-world\Python基础\7.1文件基础\Walden.txt'
with open(txts,'r',encoding='UTF-8') as f:          # 再加一个编码方式encoding='UTF-8'
    x=f.read()
print(x)

'''
遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
例如：
with open(txts,'r',encoding='utf-8',error='ignore') as f:

'''