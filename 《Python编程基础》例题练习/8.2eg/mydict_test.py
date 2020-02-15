import unittest   # 引入Python自带的unittest模块

from mydict import Dict    # 导入模块中的类

class TestDict(unittest.TestCase):   # 编写单元测试,编写一个测试类，从unittest.TestCase继承
    '''此为测试模块mydict_test.py代码'''

    def test_init(self):   #以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
        d = Dict(a=1, b='test')           # 创建实例
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):   # 对每一类测试都需要编写一个test_xxx()方法
        d = Dict()                        # 创建实例
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()                        # 创建实例
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    def test_keyerror(self):
        d = Dict()                        # 创建实例
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()                        # 创建实例
        with self.assertRaises(AttributeError):
            value = d.empty