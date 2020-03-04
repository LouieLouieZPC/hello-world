import pickle
d=dict(name='Bob',age=20,score=88)
pickle.dumps(d) # 用pickle.dumps()方法,把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件