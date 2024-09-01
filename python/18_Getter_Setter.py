
# @property(getter)
"""class Employee:
    company = "Bharat gas"
    salary = 5600
    salarybonus = 400
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    
e = Employee()
print(e.totalsalary)"""


# Setter
class Employee:
    company = "Bharat gas"
    salary = 5600
    salarybonus = 400
    
    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    
    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val - self.salary 
    
e = Employee()
print(e.totalsalary)
e.totalsalary = 5800
print(e.salary)
print(e.salarybonus)