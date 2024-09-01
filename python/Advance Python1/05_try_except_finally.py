try:
    i = int(input("Enter a number: "))
    c = 1/i
    
except Exception as e:
    print(e)
    exit()
finally:   # after executing exit() in program finally still execute
    print("WE are DOne")