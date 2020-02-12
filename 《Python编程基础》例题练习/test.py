class Screen(object):
    
    @property
    def width(self):        # 这个负责返回
        return self.awidth
    @width.setter
    def width(self,value):  # 这个负责设条件
        self.awidth=value

    @property
    def height(self):        # 这个负责返回
        return self.aheight
    @height.setter
    def height(self,value):  # 这个负责设条件
        self.aheight=value

    @property
    def resolution(self):
        return self.aheight*self.awidth
        

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')