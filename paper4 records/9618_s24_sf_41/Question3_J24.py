def Enqueue(NewData):
    global QueueData
    global QueueHead
    global QueueTail
    
    if QueueTail>=19:
        return False
    
    QueueTail+=1
    QueueData[QueueTail]=NewData
    
    if QueueHead==-1:
        QueueHead=QueueTail
        
    return True
        
def Dequeue():
    global QueueData
    global QueueHead
    global QueueTail
    
    if QueueTail<QueueHead:
        return "false"
    
    DataReturn=QueueData[QueueHead]
    QueueHead+=1
    
    return DataReturn    

def StoreItems():
    CountInvalid=0
    for i in range(10):
        Digits=input("Enter a 7-character string. ")
        CheckDigit=Digits[6]
        
        if CheckDigit!='X':
            CheckDigit=int(CheckDigit)
        Sum=(int(Digits[1])+int(Digits[3])+int(Digits[5]))*3+(int(Digits[0])+int(Digits[2])+int(Digits[4]))*1
        Result=Sum//10
        if Result==0:
            if CheckDigit=='X':
                Inserted=Enqueue(Digits[0:6])
                if Inserted: print("Successfully added.")
                else: print("Queue is already full.")
        else:
            if Result==CheckDigit:
                Inserted=Enqueue(Digits[0:6])
                if Inserted: print("Successfully added.")
                else: print("Queue is already full.")
            else:CountInvalid+=1
    
    print(f"There were {CountInvalid} invalid items entered.")


#main
QueueData=[None for _ in range(20)]
QueueHead=-1
QueueTail=-1

StoreItems()
Item=Dequeue()
if Item == "false": print("The queue is empty.")
else: print(Item)