# 2.
"""name = input("Enter your name: ")
marks = input("ENter your marks: ")
phone = input("Enter your phone numner: ")

template = "The name of the student is {} his marks are {} and phone number is {}"
output = template.format(name, marks, phone)
print(output)"""


# 3.
"""l = [str(i*7) for i in range(1, 11)]
print(l)

verticaltable = "\n".join(l)
print(verticaltable)"""


# 4. 
"""l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20, 25]
a = filter(lambda a: a%5==0, l)
print(list(a))"""


# 5.
"""from functools import reduce
l = [3,8,5,4,3]

a = reduce(max, l)
print(a)"""

# 6.