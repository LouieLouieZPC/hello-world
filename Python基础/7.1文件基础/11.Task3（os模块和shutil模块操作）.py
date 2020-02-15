import os
import shutil

file_name=r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test_file'
os.mkdir(file_name)

shutil.move(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\squares.py',
r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test_file')

shutil.move(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\date.txt',
r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test_file')

shutil.make_archive(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test_file压缩包',
'zip',
'D:\\01.Software\\GitHub\\GitHub Repository\\hello-world\\《Python编程基础》例题练习\\6.1文件基础\\test_file')