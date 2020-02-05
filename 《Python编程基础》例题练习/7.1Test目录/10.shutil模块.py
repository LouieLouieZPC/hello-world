'''
重命名是指：目标路径最后的文件名要与原路径的文件名不同，故要重命名
事先不存在是未了防止报错：当文件已存在时，无法创建该文件。
'''

'''
移动文件/文件夹：
shutil.move(现路径，目标路径)：
目标路径为指向文件夹（该文件夹事先存在）：1.无同名文件：移动2.有同名文件：重写
目标路径为指向具体文件：移动后要重命名

返回值是移动后的文件绝对路径字符串

'''

# 移动文件或文件夹
import shutil
shutil.move(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test\test',
r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test1')


'''
1.复制文件：shutil.copyfile(src路径指向具体文件,dst路径指向具体文件(重命名))，从src复制到dst，返回值是复制后的文件绝对路径字符串
2.复制文件到文件或文件目录：shutil.copy(src路径指向具体文件,dst路径指向具体文件(重命名)或目录)，从src复制到dst，返回值是复制后的文件绝对路径字符串
3.复制目录：shutil.copytree(src路径指向目录，dst路径指向目录(该目录事先不存在))，从src复制到dst，返回值是复制后的文件绝对路径字符串
'''
# 复制文件
import shutil
shutil.copyfile(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test1',
r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test2')
import shutil
shutil.copytree(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础',
r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1Test目录')

# 