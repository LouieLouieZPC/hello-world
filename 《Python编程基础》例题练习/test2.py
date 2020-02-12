class Screen(object):
  
    @property
    def width(self):
        return self.awidth

    @width.setter
    def width(self, width):
        self .awidth = width

    @property
    def height(self):
        return self.aheight

    @height.setter
    def height(self, height):
        self.aheight = height

    @property
    def resolution(self):
        return self.awidth * self.aheight

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')