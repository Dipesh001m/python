# if statement
'''a = 12
b = 10
if a > b:
    print("a is greater")'''


# elif
'''a = 30
b = 30
if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")'''

#
'''age = int(input("Enter your age :"))
if age > 18:
    print("yes")
else:
    print("No")'''

# AND
'''a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both condition are true")
else:
    print("both condition are wrong")'''

# OR
'''a = 200
b = 33
c = 500
if a > b or a < c:
    print("At least one condition are true")'''


# Not
"""a = 33
b = 200
if not a > b:
    print("a is not greater than b")"""




#  
"""a = 4
if(a == 7):
    print("yes") 
elif(a > 23):
    print("no and yes")
else:
    print("I am optional")"""



# problem
# 1. Write a program to find greatest of 4 no. entered b y the user
"""num1 = int(input("enter no 1:"))
num2 = int(input("enter no 2:"))
num3 = int(input("enter no 3:"))
num4= int(input("enter no 4:"))
if(num1>num4):
    f1 = num1
else:
    f1 = num4
    if(num2>num3):
        f2 = num2
    else:
        f2 = num3
        if(f1>f2):
            print(str(f1) + "is greatest" )
        else:
            print(str(f2) + "is greatest")"""


# 2.
"""sub1 = int(input("Enter first sub marks\n"))
sub2 = int(input("Enter second sub marks\n"))
sub3 = int(input("Enter third sub marks\n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail bcz you have less than 33% in one sub")

elif(sub1+sub2+sub3)/3 < 40:
    print("you are fail due to less per than 40%")

else:
    print("Congratulation you are pass")"""


# 3.
"""text = input("enter the text\n")
if("make a lots of money" in text):
    spam  = True

elif("click this" in text):
     spam = True

elif("subscribe this" in text):
    spam = True 
else:
    spam = False

if(spam):
    print("this text is spam")
else:
    print("this text is not spam")"""



# 4.Write a program to find wether a given username contain less than 10 character or not 
"""username = input("Enter your username :\n")
if(len(username)<10):
    print("Not containing 10 char")
else:
    print("containing 10 char")"""


# 5. Write a program to find wether  a given  name is present in the list or not 
"""names = ["Dipesh","Rajesh","mithlesh","Reyaj"]
name = input("Enter your names to check\n")
if name in names:
    print("Your name is present in the list ")
else:
    print("Your name is not present in the list")"""


# 6. Write a program to calculate a grade of student from his marks from the following schemes 90-100 EX, 80-90 A, 70-80 B, 60-70 C, 50-60 D, <50 F 
"""marks = int(input("Enter your marks\n"))

if marks>=90:
    grade = "EX"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D"
else:
    grade = "F"
    print("Your grade is " + grade)"""










