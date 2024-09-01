# Creating a list using []
a = [1,3,5,6,8]

# printing a list using print() function
print(a)

# Acess using index
print(a[3])

# change the value of list using  index
a[0] = 78
print(a)

# We can create  a list with item of different types
c = [45,"Dipesh",False,6.9]
print(c)

# List slicing 
friend = ["rajesh","reyaj","palak","pardeep","ajamat"]
print(friend[0:4])

# List method
# 1.sort
l1 = [1,3,5,7,9,4]
l1.sort()
print(l1)

# 2.Reverse
l1 = [1,4,6,3,7,8]
l1.reverse()
print(l1)

# 3. Append(45)
l1 = [1,4,6,3,7,8]
l1.append(45)          # appends function adds 45 the end of the list 
print(l1)


# 4. Insert
l1 = [1,4,6,3,7,8]
l1.insert(3,12)
print(l1)           # this will adds 12 at 3rd index

# 5. Pop
l1 = [1,4,6,3,7,8]
l1.pop(5)           # will delete the 5th index 
print(l1)

# 6. remove
l1 = [1,4,6,3,7,8]
l1.remove(4)        # will remove 4 from the list 
print(l1)



# creating Tuples()
t = (1,2,1,1,4,5)
t1 = (1,)    # Tuple with single element 
print(t1)

print(t.count(1))  #Returns no. of occurance in a tuple
print(t.index(4))



