
  
# snake water gun
import random
def gamewin(comp,you):
    #if two value are equal, declare a tie!
    if comp == you:
        return None
    
    # check for all possibilities when computer chose s
    elif comp == 's':
        if you =='w':
            return False
        elif you == 'g':
            return True
        
    # check for all possibilities when computer chose w
        elif comp == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True
            
    # check for all possibilities when computer chose g
            elif comp == 'g':
                if you == 's':
                    return False
                elif you == 'w':
                    return True
                
        
print("Comp Turn: Snake(s) Water(w) or Gun(g)")
randNo = random.randint(1,3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
    
you = input("Your Turn: Snake(s) Water(w) or Gun(g)")
a = gamewin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is tie")
elif a:
    print("you win")
else:
    print("you lose")

