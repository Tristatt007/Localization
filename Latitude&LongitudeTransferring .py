# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:37:48 2018

@author: Cheng
"""
import numpy as np
import math
R=6417
def coordinate(a,b):
    a=a/180.0*np.pi
    b=b/180.0*np.pi
    x=R*np.cos(a)*np.cos(b)
    y=R*np.cos(a)*np.sin(b)
    z=R*np.sin(a)
    return(x,y,z)
    
d0=coordinate(31.945555555555554,118.60444444444444) #camera和4个标定点的经纬度，通过coordinate计算出来它们的x,y,z坐标
d1=coordinate(31.946666666666665,118.605)
d2=coordinate(31.946666666666665,118.60527777777777)
d3=coordinate(31.946944444444444,118.60527777777777)
d4=coordinate(31.94638888888889,118.605)
'''
print(d0,'\n')
print(d1)
print(d2)
print(d3)
print(d4)
print('\n')
'''
x0=d0[0]
y0=d0[1]
z0=d0[2]

x1=d1[0]-x0
y1=d1[1]-y0
z1=d1[2]-z0

x2=d2[0]-x0
y2=d2[1]-y0
z2=d2[2]-z0

x3=d3[0]-x0
y3=d3[1]-y0
z3=d3[2]-z0

x4=d4[0]-x0
y4=d4[1]-y0
z4=d4[2]-z0


distance1=math.sqrt(x1*x1+y1*y1+z1*z1)
distance2=math.sqrt(x2*x2+y2*y2+z2*z2)
distance3=math.sqrt(x3*x3+y3*y3+z3*z3)
distance4=math.sqrt(x4*x4+y4*y4+z4*z4)
#S=R*math.pi*2[math.asin(0.5*direct/R)]/180 这里才转的话， 前面计算的direct里还是角度，所以值不对。

'''
print(x1,y1,z1,'\n')
print(x2,y2,z2,'\n')
print(x3,y3,z3,'\n')
print(x4,y4,z4,'\n')
'''
print(distance1,'\n')
print(distance2,'\n')
print(distance3,'\n')
print(distance4,'\n')
