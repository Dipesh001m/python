try:
    i = int(input("Enter a number: "))
    c = 1/i
    
except Exception as e:
    print(e)
else:   # agar try bina kisi hasal k print hojayega too else print hoga verna nahi hoga 
    print("WE were sucessful")
  