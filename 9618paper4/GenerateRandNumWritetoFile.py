# 20250611
# create a file, contain 100 integers
# summation all numbers
# finding numbers, if found, return true, otherwise return false

import random

def WritingRandNum(name):
    with open(name,"w") as n:
        for i in range(100):
            n.write(str(random.randint(1,100))+"\n")
    n.close()
    
def Summation(name):
    sum = 0
    with open(name, "r") as n:
        for i in range(100):
            sum += int(n.readline(5))
    n.close()
    return sum

def NumExistence(name,num):
    with open(name, "r") as n:
        for i in range(100):
            temp = int(n.readline(5))
            if temp == num:
                return True
    n.close()
    return False


WritingRandNum("data.txt")
print(Summation("data.txt"))
print(NumExistence("data.txt",42))