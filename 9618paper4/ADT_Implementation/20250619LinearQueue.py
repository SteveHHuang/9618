# 20250619 
# Implement linear queue using array

queue = ['*' for i in range(10)]
Headptr = 0
Tailptr = 0

def dequeue():
    global Headptr, Tailptr
    if Headptr == Tailptr:
        return "This queue is empty" 
    
    value = queue[Headptr]    
    queue[Headptr] = '*'
    Headptr += 1
    print("Successfully deleted")
    return value
    
def enqueue(num):
    global Tailptr
    if Tailptr == len(queue):
        return "This queue is full" 
    
    
    queue[Tailptr] = num
    Tailptr +=1
    return "Successfully added"
    

for i in range(11):
    print(enqueue(i))
    print(Tailptr)
    
for j in range(11):
    print(dequeue())
    print(Tailptr)

print(queue)

