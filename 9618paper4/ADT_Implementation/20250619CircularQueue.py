# 20250619 
# Implement circular queue using array

queue = ['*' for i in range(10)]
Headptr = 0
Tailptr = 0
count = 0

def dequeue():
    global Headptr, Tailptr, count
    if Headptr == Tailptr and count == 0:
        return "This queue is empty" 
    
    value = queue[Headptr]    
    queue[Headptr] = '*'
    Headptr += 1
    count -=1
    if Headptr == 10:
        Headptr = 0
    print("Successfully deleted")
    return value
    
def enqueue(num):
    global Tailptr, Headptr, count
    if Headptr == Tailptr and count == len(queue):
        return "This queue is full" 
    
    queue[Tailptr] = num
    Tailptr +=1
    count +=1
    if Tailptr == 10:
        Tailptr = 0
        
    return "Successfully added"
    
for i in range(11):
    print(enqueue(i))
    print(Tailptr)
    
for j in range(6):
    print(dequeue())
    print(Tailptr)

print(queue)

