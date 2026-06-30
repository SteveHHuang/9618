class Queue:
    def __init__(self):
        self.QueueArray=[] # DECLARE QueueArray: ARRAY[0:99] OF INTEGER
        self.HeadPointer=-1 # DECLARE HeadPointer: INTEGER
        self.TailPointer=0 # DECLARE TailPointer: INTEGER

def Enqueue(AQueue,TheData):
    if AQueue.HeadPointer==-1:
        AQueue.QueueArray[AQueue.TailPointer]=TheData
        AQueue.HeadPointer=0
        AQueue.TailPointer+=1
        return 1
    elif AQueue.TailPointer>99:
        return -1
    else:
        AQueue.QueueArray[AQueue.TailPointer]=TheData
        AQueue.TailPointer+=1
        return 1

def ReturnAllData():
    global TheQueue
    ResultStr=""
    for i in range(TheQueue.HeadPointer,TheQueue.TailPointer):
        ResultStr+=(str(TheQueue.QueueArray[i])+" ")

    return ResultStr[0:len(ResultStr)-1]

def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer==-1 or TheQueue.HeadPointer==TheQueue.TailPointer:
        return -1
    Result=TheQueue.QueueArray[TheQueue.HeadPointer]
    TheQueue.HeadPointer+=1
    return Result

#main
TheQueue=Queue()
TheQueue.HeadPointer=-1
TheQueue.TailPointer=0
for i in range(100):
    TheQueue.QueueArray.append(-1)

for i in range(10):
    Valid=False
    while not Valid:
        Num=int(input("Input a non-negative integer(An integer that is no less than 0). "))
        if Num>=0:
            Valid=True
            if Enqueue(TheQueue,Num)==-1:
                print("Queue full")
            else:
                print("Sucessfully added")
        else:
            print("The number input is invalid")

print(ReturnAllData())
print("")
for j in range(2):
    Num=Dequeue()
    if Num>-1: print(Num)
    else: print("Queue empty")
print("")
print(ReturnAllData())