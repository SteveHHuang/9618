QueueArray = ["*" for i in range(10)] # 1D array, with elements of 10, type string

HeadPointer = 0 # The head pointer, type of integer, initialised to 0
TailPointer = 0 # The tail pointer, type of integer, initialised to 0
NumberItems = 0 # # The number of items in the queue, type of integer, initialised to 0


def Enqueue(DataToAdd):
    global QueueArray, HeadPointer, TailPointer, NumberItems
    
    if NumberItems == len(QueueArray):
        return False
    
    QueueArray[TailPointer] = DataToAdd
    if TailPointer >= 9:
        TailPointer = 0
    else:
        TailPointer += 1
    NumberItems+=1
    return True

def Dequeue():
    global QueueArray, HeadPointer, TailPointer, NumberItems
    
    if NumberItems == 0:
        return "FALSE"
    
    temp = QueueArray[HeadPointer]

    if HeadPointer >= 9:
        HeadPointer = 0
    else:
        HeadPointer += 1
        
    NumberItems-=1
    return temp

for i in range(11):
    if Enqueue(input("Enter the data ")):
        print("Successfully added")
    else:
        print("Failed to add")
for i in range(2):    
    print(Dequeue())