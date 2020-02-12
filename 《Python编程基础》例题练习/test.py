class Screen(object):
    
    @property       #  # 把一个setter方法变成为score属性赋值
    def width(self):        # 这个负责返回
        return self.awidth
    @width.setter   # 把一个setter方法变成属性赋值
    def width(self,value):  # 这个负责设条件
        if not isinstance(value, int):
            raise ValueError('width must be integer')
        if value < 0:
            raise ValueError('width must > 0')
        self.awidth=value



    @property       # 把一个getter方法变成属性
    def height(self):        # 这个负责返回
        return self.aheight
    @height.setter  # 把一个setter方法变成属性赋值
    def height(self,value):  # 这个负责设条件
        if not isinstance(value, int):
            raise ValueError('height must be integer')
        if value < 0:
            raise ValueError('height must > 0')
        self.aheight=value   # 赋值


    @property        # 只定义getter方法，不定义setter方法就是一个只读属性
    def resolution(self):
        return self.aheight*self.awidth
        

# 测试:
s = Screen()
s.width = 1024  # 实际转化为s.awidth(1024)
s.height = 768  # 实际转化为s.aheight(768)
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')