# Guess the Number Game Rules :

# Objective: Guess the secret number chosen by the computer within the fewest attempts.

# ​Setup:

# The computer randomly selects a number between ​1 and 100 (inclusive).

# ​Gameplay:

# Player enter the guess as a whole number.

# After each guess, the computer will tell player if the secret number is ​higher (Too high!) or ​lower (Too low!).

# Repeat until player guess the correct number.

# ​Winning:

# When player guess correctly, the game ends and displays the number of attempts player used.

# Replay:

# Player can choose to play again or exit the game.


import random

replay = False
count = 1
ans = random.randint(1,100)

while True:
    response = int(input("Guess a number, between 1 and 100 inclusive:"))

    if response == ans:
        print("you are right!"+" you have tried for", count, "times")
        rep = int(input("Do you want to replay? If you want, press 1 to continue"))
        if rep == 1:
            replay = True
        break

    else:
        if response > ans:
                    print("Too high") 
        else:
                    print("Too low")    
        count += 1

while replay == True:

    count = 1
    ans = random.randint(1,100)
    response = int(input("Guess a number, between 1 and 100 inclusive:"))

    while True:
        response = int(input("Guess a number, between 1 and 100 inclusive:"))

        if response == ans:
            print("you are right!"+" you have tried for", count, "times")
            rep = int(input("Do you want to replay? If you want, press 1 to continue"))
            if rep != 1:
                replay = False
            break

        else:
            if response > ans:
                        print("Too high") 
            else:
                        print("Too low")    
            count += 1
                                                