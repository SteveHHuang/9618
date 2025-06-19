# 20250619 
# Implement queue using array

queue = [i for i in range(10)]
Headptr = 0
Tailptr = queue[len(queue)-1]

def dequeue():
    global Headptr, Tailptr
    if Headptr > Tailptr:
        Headptr = Tailptr
        return "This queue is empty" 
        
    queue[Headptr] = '*'
    Headptr += 1
    return "Successfully deleted"
    
def enqueue(num):
    global Tailptr
    if Tailptr > len(queue)-1:
        return "This queue is full" 
    
    queue[Tailptr] = num
    Tailptr +=1
    return "Successfully added"
    

for i in range(11):
    print(dequeue())
    print(Headptr)

print(queue)

