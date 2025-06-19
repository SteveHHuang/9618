# 20250619 
# Implement circular queue using array

queue = ['*' for i in range(10)]
Headptr = 0
Tailptr = 0
enqueued = False

def dequeue():
    global Headptr, Tailptr
    if Headptr == Tailptr:
        return "This queue is empty" 
        
    queue[Headptr] = '*'
    Headptr += 1
    if Headptr == 10:
        Headptr = 0
    
    return "Successfully deleted"
    
def enqueue(num):
    global Tailptr, Headptr, enqueued
    
    if enqueued == True:
        if Headptr == Tailptr:
            return "This queue is full" 
    
    queue[Tailptr] = num
    Tailptr +=1
    if Tailptr == 10:
        Tailptr = 0
    enqueued = True
        
    return "Successfully added"
    


print(queue)

