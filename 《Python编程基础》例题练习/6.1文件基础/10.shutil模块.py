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



'''
1.os.unlink()/os.remove()删除文件
2.os.rmdir()删除一个空目录
3.shutil.rmtree()删除一个目录及其所有内容
'''
import os
import shutil
os.unlink(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test2')
os.rmdir(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\6.1文件基础\test')
shutil.rmtree(r'D:\01.Software\GitHub\GitHub Repository\hello-world\《Python编程基础》例题练习\7.1Test目录')


'''
1.压缩(将文件夹压缩到文件中)：
shutil.make_archive(base_name,format,root_dir,owner,group,logger)函数：

base_name： 压缩包的文件名，也可以是压缩包的路径。如果不指定绝对路径，只是文件名时，则保存至当前目录，否则保存至指定路径，路径指向文件名！！！
                        如：www                        =>保存至当前路径
                        如：/Users/aaa/www =>保存至/Users/aaa/
format  ：   压缩包种类，“zip”, “tar”, “bztar”，“gztar”,“xztar”
root_dir：   要压缩的文件夹路径（默认当前目录）,路径指向文件夹！！！！！
owner   ：   用户，默认当前用户
group   ：   组，默认当前组
logger  ：   用于记录日志，通常是logging.Logger对象
'''
# 压缩文件
import shutil
shutil.make_archive(r'C:\Users\66435\OneDrive\桌面\Iris数据集\哈哈哈','zip',r'C:\Users\66435\OneDrive\桌面\Iris数据集')





'''
 2.解压（将压缩包解压到文件夹中）：
 shutil.unpack_archive(filename[, extract_dir[, format]])函数：
 解压缩或解包源文件。
filename是压缩文档的完整路径，路径指向文件名，加格式后缀！！！
extract_dir是解压缩路径，默认为当前目录，路径指向文件夹！！！
format是压缩格式。默认使用文件后缀名代码的压缩格式。
'''
# 解压文件
import shutil
shutil.unpack_archive(r'C:\Users\66435\OneDrive\桌面\Iris数据集\Titanic.zip',
r'C:\Users\66435\OneDrive\桌面\压缩包文件夹')
