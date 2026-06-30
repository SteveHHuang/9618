def Enqueue(DataToAdd):
    global QueueArray
    global HeadPointer,TailPointer,NumberItems
    
    if NumberItems==10: return False

    QueueArray[TailPointer]=DataToAdd
    if TailPointer>=9:
        TailPointer=0
    else:
        TailPointer+=1
    NumberItems+=1
    
    return True

def Dequeue():
    global QueueArray
    global HeadPointer,TailPointer,NumberItems
    
    if NumberItems==0: return "FALSE"
    
    ReturnItem=QueueArray[HeadPointer]
    if HeadPointer>=9:
        HeadPointer=0
    else:
        HeadPointer+=1
    NumberItems-=1
    
    return ReturnItem

#main
QueueArray=["" for _ in range(10)] #DECLARE QueueArray: ARRAY[1:10] OF STRING
HeadPointer=0 #DECLARE HeadPointer: INTEGER
TailPointer=0 #DECLARE TailPointer: INTEGER
NumberItems=0 #DECLARE NumberItems: INTEGER

for j in range(11):
    if Enqueue(input("Enter the data to the queue\n")): print("Successfully added.")
    else: print("Queue is full, failed to add.")

print(Dequeue())
print(Dequeue())