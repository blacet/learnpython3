# -*- coding: utf-8 -*-

class Screen(object):

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution