'''
Created on 7 Oct 2017

@author: matt
'''

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "Point: (%d, %d, %d)" % (self.x, self.y, self.z)
    
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, " Point deleted ")
        
    @property
    def x(self):
        "I am the 'x' property."
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
    
    @x.deleter
    def x(self):
        del self._x        
    
    @property
    def y(self):
        "I am the 'y' property."
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @y.deleter
    def y(self):
        del self._y    
    
    @property
    def z(self):
        "I am the 'z' property."
        return self._z
    
    @z.setter
    def z(self, value):
        self._z = value
    
    @z.deleter
    def z(self):
        del self._z 
    
    
    
    
    