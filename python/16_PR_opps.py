
# 1.
'''class programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
        
dipesh = programmer("DIpesh", "Skype")
rajesh = programmer("Rajesh", "Github")
dipesh.getInfo()
rajesh.getInfo()'''


# 2.
"""class calculator:
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
        
    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")
        
    def cube(self):
        print(f"The value of {self.number} Cube is {self.number **3}")

    
a = calculator(9)
a.square()
a.squareRoot()
a.cube()"""


# 3.
"""class Sample:
    a = "DIpesh"
    
obj = Sample()  # this is object instance and it does not change class attribute while class and obj name is sample 
obj.a = "Dipesh"   # this set new instance attribute
#Sample.a = "Rajesh"  #this change class attribute

print(Sample.a)
print(obj.a)"""


# 4.
"""class calculator:
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
        
    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **0.5}")
        
    def cube(self):
        print(f"The value of {self.number} Cube is {self.number **3}")
        
    @staticmethod
    def greet():
        print("Hello everyone welcome to calculator")

    
a = calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()"""



# 5.
class Train:
    def __init__(self, name , fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def getStatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The Seats available in the train are: {self.seats}")
        
    def fareInfo(self):
        print(f"The price of the ticket is Rs: {self.fare}")
        
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your Ticket has been booked! Your seats number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is full! Kindly try in tatkal!")
        
        
rajdhani = Train("Rajdhani Express: 14015", 90, 3)
rajdhani.getStatus()
rajdhani.bookTicket()
rajdhani.bookTicket()
rajdhani.bookTicket()
rajdhani.getStatus()
        
    



        