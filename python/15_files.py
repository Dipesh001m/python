
# Create  a new txt file and write content on them
'''f = open("this.txt","w")
f.write("Hey Dipesh how are you")
f.close()'''



# Read that content
'''f = open("this.txt", "r")
#text = f.read()
text = f.read(5)     # Read the first 5 character
print(text)
f.close()'''


# Readline function
'''f = open("this.txt","r")
text = f.readline()   # reads first line this.txt
print(text)
text = f.readline()   # reads seocnd lines of this.txt
print(text)
f.close()'''


# With statement
'''with open("this.txt", "r") as f:
    text = f.read()
    print(text)'''
    
    
# 1 problem
#f = open("poems.txt","w")
#f.write("twinkle twinkle little star how i wonder what you are!")

'''f = open("poems.txt")
t = f.read()
if "twinkle" in t:
    print("twinkle is present")
else:
    print("twinkle is not present")
    f.close()'''
    
    



# 6.
'''with open("log.txt") as f:
   content = f.read()
    
if "jaipur" in content.lower():
    print("yes jaipur is present")
else:
    print("jaipur is not present")'''
    
    

# 7.
'''content = True
i = 1
with open("log.txt") as f:
    while content:
        content = f.readline()
        if "jaipur" in content.lower():
            print(content)
            print(f"yes jaipur is present on line number {i}")
            i += 1'''
            
            
# 8. Write a program t make copy of a text file "this.txt"

'''with open("this.txt") as f:
    content = f.read()
    
with open("copy.txt", "w") as f:
    f.write(content)'''
    
    
# 9.Write a program to find out whether a files are identitical or not 

'''files1 = "log.txt"
files2 = "this.txt"

with open(files1) as f:
    f1 = f.read()
    
with open(files2) as f:
    f2 = f.read()
    
if f1 == f2:
    print("Files are identical")
else:
    print("files are not identical")'''
    
    

# 10. write a program to wipe out a content of file ( wipe means to delete a file content )

'''filename = "poems.txt"   # it delete all files which present in poems.txt
with open(filename,"w") as f:
    f.write("")'''
    
    

# 11. Write a program to rename a file to "remove_by_python.txt"


