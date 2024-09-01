"""try:
    a = int(input("Enter a number:"))
    c = 1/a
    print(c)
except Exception as e:
    print("Exception occured")
    print(e)
    
    print("Thanks for using this code")"""
    
    
# 
try:
    a = int(input("Enter a number:"))
    c = 1/a
    print(c)
    
except ValueError as e:
    print("Please Enter a valid value")
    
except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")
    
print("Thanks for using this code")