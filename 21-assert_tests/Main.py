'''
Created on 7 Oct 2017

@author: matt
'''
#from basic import Point, Line, Plane

import unittest
import basic

class Tests(unittest.TestCase):
    
    def test_is_point(self):
        self.a = basic.Point.Point(0,0,1)
        self.assertTrue(type(self.a) is basic.Point.Point, "is point")
        #self.assertEqual()
        
    @unittest.expectedFailure
    def test_is_line(self):
        self.b = basic.Point.Point(0,0,1)
        self.assertTrue(type(self.b) is basic.Line.Line, "obj. not line")
    
    def test_is_no_line_in_line(self):
        self.c = basic.Line.Line(basic.Point.Point(1,1,1), basic.Point.Point(1,2,1))
        self.assertEqual(self.c.lenght(), 0, "obj. not line is point")
        
    
    
if __name__ == '__main__':
    
    unittest.main()
    
    """    
    import basic
    
    point_1 = basic.Point.Point(0,0,1)
    
    print(point_1)
    
    point_2 = basic.Point.Point(3,4,0)
    print(point_1)
    
    line_1 = basic.Line.Line(point_1,point_2)
    print(line_1)
    
    print(line_1.lenght())
    """ 
    
    