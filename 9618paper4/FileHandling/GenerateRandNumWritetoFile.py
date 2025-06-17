# 20250611
# create a file, contain 100 integers
# summation all numbers
# finding numbers, if found, return true, otherwise return false

import os
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # 获取脚本所在目录的绝对路径

def WritingRandNum(name):
    filepath = os.path.join(SCRIPT_DIR, name) # 拼接txt文件路径
    with open(filepath,"w") as n:
        for i in range(100):
            n.write(str(random.randint(1,100))+"\n")
    n.close()
    
def Summation(name):
    sum = 0
    filepath = os.path.join(SCRIPT_DIR, name)

    with open(filepath, "r") as n:
        for i in n:
            sum += int(i.strip())
    n.close()
    return sum

def NumExistence(name,num):
    filepath = os.path.join(SCRIPT_DIR, name)

    with open(filepath, "r") as n:
        for i in range(100):
            temp = int(n.readline(5))
            if temp == num:
                return True
    n.close()
    return False


WritingRandNum("data.txt")
print(Summation("data.txt"))
print(NumExistence("data.txt",42))