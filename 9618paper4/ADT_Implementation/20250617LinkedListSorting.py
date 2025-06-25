#Implement Linked list using 2D array

import random

#Step1: initialise a 2D array to implement linked list, 10rows, 2 columns
LinkedList = [[0, i] for i in range(1,11)]
LinkedList[9][1] = -1
# print(LinkedList)

# Step2: Initialize headpointer, freeptr
headptr = -1 # headptr always point to the address of the first used node
freeptr = 0 # freeptr always point to the address of first free space

# Step3: Adding value
def addDatainSeq(val): # In descending order
    global headptr, freeptr, LinkedList
    if freeptr == -1:
        return "no space"
    
    if headptr == -1:
        headptr = freeptr
        freeptr = LinkedList[freeptr][1] # freeptr always point to the first free space
        LinkedList[headptr][0] = val
        LinkedList[headptr][1] = -1 # 添加第一个数据的时候 因为后面没有数据 所以第一个node的ptr是-1
        return "successfully added"
          
    temp = freeptr # address of the new node
    freeptr = LinkedList[freeptr][1]
    # LinkedList[nextPlaceToAdd][1] = temp # -1 to temp
    LinkedList[temp][0] = val
    
    if LinkedList[temp][0] >= LinkedList[headptr][0]:
        LinkedList[temp][1] = headptr
        headptr = temp
        return "successfully added"

    nextPlaceToAdd = headptr
    
    while LinkedList[nextPlaceToAdd][1] != -1 and LinkedList[LinkedList[nextPlaceToAdd][1]][0] >= val:
        nextPlaceToAdd = LinkedList[nextPlaceToAdd][1]
        
    LinkedList[temp][1] = LinkedList[nextPlaceToAdd][1] # 插入新节点
    LinkedList[nextPlaceToAdd][1] = temp
    return "successfully added"
        
        
        
for i in range(10):         
    addDatainSeq(random.randint(1,1000))
    # addData(19)
    print(LinkedList)
   
   
def searchNum(num, arr):  
    for j in range (10):
        if arr[j][0] == num:
            return j
        return -1


print(LinkedList)    
# print(searchNum(228, LinkedList))
   