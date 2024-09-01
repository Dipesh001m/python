# Perfect guess

import random
randNumber = random.randint(1, 100)
print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You gussed it wrong! Enter a large number")
            
print(f"You guessed the number in {guesses}guesses")
with open("highscore.txt", "r") as f:
     highscore = int(f.read())
if(guesses<highscore):   # it store the highscore in highscore txt file in memory
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))

        
        
        
    