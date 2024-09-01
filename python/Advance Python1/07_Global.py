
a = 54 # Global variable
def fun1():
    global a
    print(f"print statement1: {a}")
    
    a = 8 # Local variable
    print(f"print statement2: {a}")
    
fun1()
print(f"print statement3: {a}")