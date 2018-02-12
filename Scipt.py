
import point
import Inheritance
import Overloading
class Employee:
        'Common base class for all employees'
        empCount = 0
        def __init__(self, name, EmpID , salary, Age , Address):
            self.name = name
            self.EmpID = EmpID
            self.salary = salary
            self.Address = Address
            self.Age = Age
            Employee.empCount += 1
        def displayCount(self):
            print ("Total Employee %d" % Employee.empCount)
        def displayEmployee(self):
            print ("Name : ", self.name,"Employee ID : ", self.EmpID,"Age : ", self.Age,"Address : ", self.Address, ", Salary: ", self.salary)
            print("Does Employee : ",getattr(self, "name"), " Has Salary ",hasattr(self, "salary"))
            setattr(self, 'salary', 77000)
            print ("Name : ", self.name,"Employee ID : ", self.EmpID,"Age : ", self.Age,"Address : ", self.Address, ", Salary: ", self.salary)
#This would create first object of Employee class"
emp1 = Employee("Abhishek", 310744,67000,32,802)
emp2 = Employee("Arpita", 310799,68000,33,803)
emp3 = Employee("Aaradhya", 310755,69000,34,804)
emp4 = Employee("Akhilesh", 310766,70000,35,805)
#This would create second object of Employee class"
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
print("Total Number of Employee in Organization : ", Employee.empCount)

print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

pt1 = point.Point()
pt2 = pt1
pt3 = pt1

#########################

c = Inheritance.Child()
c.ChildMethod()
c.ParentMethod()
print("New Value Before calling Setatt",c.getatt())
c.setatt(500)
print("New Value after calling Setatt",c.getatt())
p = Inheritance.Parent()
p.ParentMethod()
#########################

c = Overloading.Child() # instance of child
c.myMethod() # child calls overridden method
p = Overloading.Parent()
p.myMethod()


