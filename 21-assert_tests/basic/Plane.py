'''
Created on 8 Oct 2017

@author: matt
'''

class Plane(object):
    '''
    classdocs
    '''


    def __init__(self, point_1, point_2, point_3):
        '''
        Constructor
        '''
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        
    def smf(self):
        return ( ((self.dot_1.x-self.dot_2.x-self.dot_3.x)**2)
                 + ((self.dot_1.y-self.dot_2.y-self.dot_3.y)**2)
                 + ((self.dot_1.z-self.dot_2.z-self.dot_3.z)**2))**0.5