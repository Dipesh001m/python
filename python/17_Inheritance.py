"""class Employee:  # Employee is Base Class
    company = "Google"
    
    def showDetails(self):
        print("This is an Employee")
    company = "Youtube"
        
class programmer(Employee): # programmer is child class of Base class
    language = "Python"       
    def getlanguage(self):
        print(f"The language is {self.language}")
        
e = Employee()
e.showDetails()
p = programmer()
p.showDetails()
print(p.company)"""  # it will print inheritance class company instead of base class if there is not company in child 
                  # class than only print base class comapny 
                  


          
# Single Inheritance
"""class Employee:  # Employee is Base Class
    company = "Google"
    
    def showDetails(self):
        print("This is an Employee")
    company = "Youtube"
        
class programmer(Employee): # programmer is child class of Base class or Called single inheritance
    language = "Python"       
    def getlanguage(self):
        print(f"The language is {self.language}")
        
e = Employee()
e.showDetails()
p = programmer()
p.showDetails()
print(p.company)"""


# Multiple inheritance
"""class freelancer:   # Base/Parent class
    company = "Fiverr"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1
        
class Employee:   # Base/Parent class
    company = "Visa"
    ecode = 120
    
class Programmer(freelancer, Employee):  # multiple inheritance alse called child class
    name = "Dipesh"
    
p = Programmer()
p.upgradeLevel()
print(p.company)"""



# MultiLevel Inheritance
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







