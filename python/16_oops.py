
# class
'''class employee:
    x = 2
print(employee)'''

# Object
'''class employee:
    x = 5
dipesh = employee()
print(dipesh.x)'''


# Railways form example
'''class railwayform:
    formType = "railwayform"
    def printData(self):   # function define
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")
        

dipeshApplication = railwayform()
dipeshApplication.name = "Dipesh"
dipeshApplication.train = "Rajdhani express"
dipeshApplication.printData()'''


# 
'''class Employee:
    company = "Google"   # this is class attribute
    
dipesh = Employee()
rajesh = Employee()
print(dipesh.company)
print(rajesh.company)

dipesh.salary = 100000  # this is instance attribute


Employee.company = "Youtube"   # we change class  attribute by applying (.)
print(dipesh.company)
print(rajesh.company)

print(dipesh.salary)  '''



# Self parameter
'''class Employee:
    comapny = "Google"
    def getsalary(self):
        print("salary is 1000k")
    
dipesh = Employee()
dipesh.getsalary()'''


# Static method
'''class Employee:
    company = "Google"
    def getsalary(self, signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")
        
    @staticmethod
    def greet():
        print("good morning dipesh")
    
dipesh = Employee() 
dipesh.salary = 100000  
dipesh.getsalary("thanks") # Employee.getsalary(dipesh)
dipesh.greet() # Employee.greet()'''


# __init__() constructor
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dipesh = Employee("Dipesh", 23)
print(dipesh.name)
print(dipesh.age)

            

