#Implement Linked list using 2D array

import random

#Step1: initialise a 2D array to implement linked list, 10rows, 2 columns
LinkedList = [[0, i] for i in range(1,11)]
LinkedList[9][1] = -1
# print(LinkedList)

# Initialize headpointer, freeptr

headptr = -1 # headptr always 
freeptr = 0 # freeptr always point to the first free space

def addData(val):
    global headptr, freeptr, LinkedList
    if freeptr == -1:
        return "no space"
    
    if headptr == -1:
        headptr = freeptr
        freeptr = LinkedList[freeptr][1] # freeptr always point to the first free space
        LinkedList[headptr][0] = val
        LinkedList[headptr][1] = -1 # 添加第一个数据的时候 第一个node的ptr是-1
        return "successfully added"
        
    PlaceToAdd = headptr
    while LinkedList[PlaceToAdd][1] != -1:
        PlaceToAdd = LinkedList[PlaceToAdd][1]
    
    temp = freeptr # address of the new node
    freeptr = LinkedList[freeptr][1]
    LinkedList[PlaceToAdd][1] = temp
    LinkedList[temp][0] = val
    LinkedList[temp][1] = -1
    

for i in range(10):         
    addData(random.randint(1,1000))
   
   
def searchNum(num, arr):  
    for j in range (10):
        if arr[j][0] == num:
            return j
        return -1


print(LinkedList)    
print(searchNum(228, LinkedList))
   