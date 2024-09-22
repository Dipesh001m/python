# function call
'''def my_function():
    print("Hello python")

my_function()'''

# Function argument
'''def my_function(fname):
    print("Goodmorning",fname)

my_function("DIpesh")    # This is called function with argument
my_function("Rajesh")'''


# number of argument
'''def my_function(fname, lname):
    print(fname +  " " + lname)
my_function("Dipesh", "mandal")'''


# Default parameter
'''def my_function(country = "Nepal"):
    print("i am from",country)
my_function("sweden")
my_function("india")
my_function()
my_function("brazil")'''


# write a program to using function to find greatest number among three number
'''def maximum(a,b,c):
    list = [a,b,c]
    return max(list)
a = 10
b = 15
c = 20
print(maximum(a,b,c))'''


#  Convert celsius to fahrenhit
'''def farh(cel):
    return(cel *(9/5)) + 32

c = 0
f = farh(c)
print("Fahreheit Temperature is " + str(f))'''


# sum of natural number by recursion method
def sum(n):
    if(n==1):
        return 1
    n = n + sum(n-1)
    return n
num = int(input("Enter the natural number: "))
i = sum(num)
print(i)





