# Super Method
"""class person:   # Parent class
    country = "India"
    
    def takeBreadth(self):
        print("I am breathing...")
        
class Employee(person):   # child class inherit from Base blass i.e parent
    company = "Honda"
    
    def getSalary(self):
        print(f"Salary is {self.salary}")
        
    def takeBreadth(self):
        print("I am Employee so i am breathing.....")
        
        
class programmer(Employee):   # child class inherit from Base blass i.e Employee
    company = "Fiver"
    
    def getSalary(self):
        print(f'No salary to programmers')
        
    def takeBreadth(self):
        super().takeBreadth()  # SUPER first runs its Super Base class than after it runs its class
        print("I am programmer so i am breadthing....")
     
# Object Declration   
p = person()
p.takeBreadth()
print(p.country)

e = Employee()
e.takeBreadth()
print(e.company)

pr = programmer()
pr.takeBreadth()  # Programmer inherrit from Employee so it print EMployee function
print(pr.company)"""



# Class method
"""class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"
    
    @classmethod
    def changesalary(cls, sal):
        cls.salary = sal
    
e = Employee()
print(e.salary)
e.changesalary(455)
print(e.salary)
print(Employee.salary)"""