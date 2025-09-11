#!/usr/bin/env python3

# File Name: TestTriangle

import random

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c
    
    def setA(self, a):
        self.a = a
        
    def setB(self, b):
        self.b = b
        
    def setC(self, c):
        self.c = c
       
    def area(self):
        area = (self.a ** 2 + self.b ** 2 + self.c ** 2)
        return area
    
    def getATriangle(self, a, b, c):
        t = Triangle(a,b,c)
        return t
    
    def __str__(self):
        return ("Triangle is constructed with ({0},{1},{2})".format(self.a, self.b, self.c))
    
def main():
    a = random.randint(0,10)
    b = random.randint(0,10)
    c = random.randint(0,10)
    
    t = Triangle(a,b,c)
    areaT = t.area()
    
    
    print(str(t))
    print()
    print("Area of Triangle t is {0}".format(areaT))

main()