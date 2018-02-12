'''
Created on Feb 12, 2018

@author: Administrator
'''
class Parent:
    parentAttr = 100
    
    def __init__(self):
        print("Inside Parent Constructure")
    
    def ParentMethod(self):
        print("Caling Parent Mehtod")
    
    def setatt(self,value):   
        Parent.parentAttr = value  
        
    def getatt(self):   
        return(Parent.parentAttr)
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    
class Child(Parent):
    
    def __init__(self):
        print("Inside Child Constructure Hello world")
        
    
    def ChildMethod(self):
        print("Caling Child Mehtod")   
    
    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "destroyed")
    
    