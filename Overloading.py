'''
Created on Feb 12, 2018

@author: Administrator
'''
class Parent: # define parent class
    def myMethod(self):
        print ('Calling parent method in Overloading')
class Child(Parent): # define child class
    def myMethod(self):
        print ('Calling child method in Overloading')
#===============================================================================
# c = Child() # instance of child
# c.myMethod() # child calls overridden method
# p = Parent()
# p.myMethod()
#===============================================================================