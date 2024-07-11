import random

target = random.randint(1 , 100)

while True :
    userGuess = input("Guess the correct number or Quit : ")

    if userGuess == "Quit" :    
        break

    userGuess = int(userGuess)

    if userGuess == target :
        print("You guessed it Correct ✨✨")
        break
    elif userGuess > target :
        print("Your guess is much bigger. Try again")
    elif userGuess < target :
        print("Your guess is much smaller. Try again")

print("-----Game Over-----")