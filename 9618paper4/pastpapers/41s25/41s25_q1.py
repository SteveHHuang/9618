Queue = [-1 for i in range(20)]

HeadPointer = -1 # Global variable of integer type, initialised to –1, points to the first element in the queue.
TailPointer = -1 # Global variable of integer type, initialised to –1, points to the last element in the queue
NumberItems = 0 # Global variable of integer type, initialised to 0, stores the number of items in the queue.


def Enqueue(num):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 20:
        return False
    
    temp = NumberItems
    
    NumberItems+=1
    Queue[NumberItems-1] = num
    
    if TailPointer == len(Queue)-1:
        TailPointer = 0    
        
    else: 
        TailPointer +=1
    
    if temp == 0:
        HeadPointer = TailPointer
    
    return True
    
for i in range(1, 26):
    if Enqueue(i): print(f"{i} Successful")
    else: print(f"{i} Unsuccessful")
    

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems == 0: return -1
    
    data = Queue[NumberItems-1]
    NumberItems -=1
    
    if HeadPointer == len(Queue)-1:
        HeadPointer = 0
    else:
        HeadPointer +=1
    
    return data

print(Dequeue())
print(Dequeue())