HeadPointer = -1 # Stores the index of the first element in the Queue, initialised to -1
TailPointer = -1 # Stores the index of the last element in the Queue, initialised to -1
Queue = [-1 for i in range(50)] # Global 1D array to type integer, all elements are initialised to -1

def Enqueue(num):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 49:
        return False
    
    TailPointer +=1
    
    if HeadPointer == -1:
        HeadPointer = TailPointer
        
    Queue[TailPointer] = num
    return True

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer >= TailPointer or HeadPointer == -1:
        return -1
    
    data = Queue[HeadPointer]
    HeadPointer+=1
    return data

def CreateQueue():
    global Queue, HeadPointer, TailPointer
    try:
        f = open("QueueData.txt", 'r')
        while True:
            tempstr = f.readline().strip()
            if tempstr == '':
                break
            temp = int(tempstr)
            if not Enqueue(temp):
                print("Queue full")
                break
        f.close()
        
    except: 
        print("error")
        

CreateQueue()

sum = 0
for i in range(len(Queue)):
    num = Dequeue()
    if num == -1:
        continue
    else:
        sum+=num
    
print(sum)