global Queue # DECLARE Queue: ARRAY[0:19] OF INTEGER
global HeadPointer
global TailPointer
global NumberItems

def Enqueue(Num):
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    
    if NumberItems>=20:
        return False
    
    NumberItems+=1
    TailPointer+=1
    if TailPointer>=20:
        TailPointer=0
    if HeadPointer==-1:
        HeadPointer=0
    Queue[TailPointer]=Num
    return True

def Dequeue():
    global Queue
    global HeadPointer
    global TailPointer
    global NumberItems
    
    if NumberItems<=0:
        return -1
    
    NumberItems-=1
    Item=Queue[HeadPointer]
    HeadPointer+=1
    if HeadPointer>=20:
        HeadPointer=0
    
    return Item
       

#main
Queue=[-1 for _ in range(20)]
HeadPointer=-1
TailPointer=-1
NumberItems=0

for i in range(1,26):
    if Enqueue(i): print(f"{i} Successful")
    else: print(f"{i} Unsuccessful")

print(Dequeue())
print(Dequeue())

print(HeadPointer,TailPointer,NumberItems)