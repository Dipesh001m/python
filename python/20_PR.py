# 1.
"""class c2dvec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    
    
class c3dvec(c2dvec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
        
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = c2dvec(1,3)
v3d = c3dvec(1,9,7)
print(v2d)
print(v3d)"""


# 2.
"""class Animals:
    animaltype = "Mammal"
    
class pets:
    color = "white"
    
class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!")
        
d = Dog()
d.bark()"""


# 3.
"""class Employee:
    salary = 1000
    increment = 1.5
    
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai/self.salary
        
e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)"""


# 5.
"""class vector:
    def __init__(self, vec):
        self.vec = vec
        
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newlist = []
        for i in range(len(self.vec)):
            newlist.append(self.vec[i] + vec2.vec[i])
        return vector(newlist)
    
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
        
        
        
v1 = vector([1, 4, 5])
v2 = vector([1, 6, 6])
print(v1+v2)
print(v1*v2)"""


# 6.
"""class vector:
    def __init__(self, vec):
        self.vec = vec
        
    def __str__(self):  
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        
               
v1 = vector([1, 4, 5])
v2 = vector([1, 6, 6])
print(v1)
print(v2)"""

