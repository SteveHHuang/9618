#20250609
import random
import printdata as pd
#randomly select ball from two different boxes 
#each boxes contains 50 red balls and 50 black balls
sumrborbr = 0
sumbb = 0
sumrr = 0

def generateBallBox():
    box1 = [] 
    box2 = [] 

    for i in range(50):
        box1.append('R')
        box2.append('R')
    for j in range(50):
        box1.append('B')
        box2.append('B')
    random.shuffle(box1)
    random.shuffle(box2)
    return box1,box2

def pickup(box1, box2):
    resultarr=[]
    for k in range(100,0,-1):
        index1 = random.randint(0,k-1)
        index2 = random.randint(0,k-1)
        resultarr.append(box1.pop(index1)+box2.pop(index2)) # pop之后
        
        return resultarr

def countprobability(resultarr):
    countRBorBR = 0
    countBB = 0
    countRR = 0
    for c in resultarr:
        if c == 'RB' or c == 'BR':
            countRBorBR += 1
        if c == 'BB' :
            countBB += 1
        if c == 'RR' :
            countRR += 1
    
    return countRBorBR,countBB,countRR


for q in range(50000): #计多次取平均
    resultbox1,resultbox2 = generateBallBox()
    result = pickup(resultbox1,resultbox2)
    temprborbr,tempbb,temprr = countprobability(result) #用逗号来分别把返回值赋给不同的变量
    sumrborbr +=temprborbr
    sumbb +=tempbb
    sumrr +=temprr

avgrborbr = sumrborbr/50000
avgbb = sumbb/50000
avgrr = sumrr/50000

print(avgrborbr)
print(avgbb)
print(avgrr)

# for j in range(0,100):
#     i1 = random.randint(0,1)
#     i2 = random.randint(0,1)
#     i3 = i1 + i2
    
#     box1[i1] -= 1
#     box2[i2] -= 1
    
#     resultarr.append(i3)
    
# for k in resultarr:
#     if k == 1:
#         countRBorBR +=1
#     if k == 0:
#         countRR +=1
#     if k == 2:
#         countBB +=1
        
# print(countRBorBR)
# print(countBB)
# print(countRR)
# print(box1)
# print(box2)
