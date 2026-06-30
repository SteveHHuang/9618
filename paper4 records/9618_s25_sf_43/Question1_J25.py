global HeadPointer
global TailPointer
global Queue # DECLARE Queue: ARRAY[0:49] OF INTEGER

def Enqueue(Num):
    global HeadPointer
    global TailPointer
    global Queue
    
    if TailPointer>=len(Queue)-1:
        return False
    if TailPointer==-1:
        HeadPointer=0
    
    TailPointer+=1
    Queue[TailPointer]=Num
    return True

def Dequeue():
    global HeadPointer
    global TailPointer
    global Queue
    
    if HeadPointer==-1 or HeadPointer>TailPointer:
        return -1
    
    HeadPointer+=1
    return Queue[HeadPointer-1]

def CreateQueue():
    try:
        f=open("QueueData.txt",'r')
        for line in f:
            if not Enqueue(int(line.strip())):
                print("Queue full")
        f.close()
    except IOError:
        print("File not found.")

#main
Queue=[-1 for _ in range(50)]
HeadPointer=-1
TailPointer=-1

CreateQueue()
Sum=0
for i in range(len(Queue)):
    Temp=Dequeue()
    if Temp!=-1:
        Sum+=Temp
print(f"Total: {Sum}")
