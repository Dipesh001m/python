# 2.
"""l = [1,2,3,4,5,6,7,8,9,10]
for index, item, in enumerate(l):
    if index==2 or index==4 or index==6:
        print(index, item)"""
        #print(f"The {index + 1}th element is {item}")
        
        
# 3.
"""num = int(input("Enter your number: "))
table = [num*i for i in range(1, 11)]
print(table)"""


# 4.
"""a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
try:
    print(a/b)
except:
    print("Infinite")"""
    
    
# 5.
num = int(input("Enter your number: "))
table = [num*i for i in range(1, 11)]
print(table)
with open("table.txt", "a") as f:
    f.write(str(table))
    f.write("\n")
