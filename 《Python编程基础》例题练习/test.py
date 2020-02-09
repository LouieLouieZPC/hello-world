# -*-coding:utf-8-*-

def normalize(name):
    return name.capitalize()
print(list(map(normalize,['adam', 'LISA', 'barT'])))
['Adam', 'Lisa', 'Bart']

from functools import reduce
print(reduce(lambda x,y: x*y,[3, 5, 7, 9]))
945

from functools import reduce
digits={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        reduce(,reduce(lambda x:digits[n],n))