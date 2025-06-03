# 100以内加减法
import random

try:
    mark = 0
    StopPlaying = False

    def RandNumSummation(num1, num2):
            return num1 + num2

    while StopPlaying == False:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        ans = RandNumSummation(num1, num2)
        print("Calculate:", num1, "+", num2)
        correctAns = False
        while correctAns == False:
            response = int(input("input your answer:"))
            if response == ans:
                mark += 1
                correctAns = True
                print("correct")
                replay = int(input("want to play again?" + "press 1 to continue.\n"))
                if replay != 1:
                    StopPlaying = True
            else:
                print("incorrect, try again")

    print("You got", mark, "mark(s)")

except:
    print("invalid input, automatically stopped playing")