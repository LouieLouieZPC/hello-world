from multiprocessing import Pool
import os,time,random    # 导入os、time、random模块

def long_time_task(name):
    print('Run task %s(%s)'%(name,os.getpid()))
    start=time.time()       # time.time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
    time.sleep(random.random()*3)        # time sleep(secs) 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。;random() 方法返回随机生成的一个实数，它在[0,1)范围内
    end=time.time()         #
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))   # %0.2f为round（）四舍五入后保留两位小数

if __name__ == "__main__":
    print('Parent process %s.'%os.getpid())
    p=Pool(4)   # 这里设定了可同时跑4个进程，若改成p = Pool(5)则可同时跑5个进程；Pool的默认大小是本电脑CPU的核数
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()  # 对Pool对象调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')


'''
# Output:
Parent process 17812.
Waiting for all subprocesses done...
Run task 0(17100)
Run task 1(19100)
Run task 2(17320)
Run task 3(18472)
Task 0 runs 0.42 seconds.
Run task 4(17100)
Task 2 runs 1.86 seconds.
Task 4 runs 1.60 seconds.
Task 3 runs 2.09 seconds.
Task 1 runs 2.66 seconds.
All subprocesses done.
'''

因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程
所以在输出的结果中，task 4要等待前面某个task完成后才执行