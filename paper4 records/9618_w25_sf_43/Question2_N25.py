global Queue # DECLARE Queue: ARRAY[0:99] OF STRING
global QueueHead
global QueueTail
global NumberItems
global NewString


def Enqueue(NewItem):
    global Queue
    global QueueHead
    global QueueTail
    global NumberItems

    if NumberItems>=100:
        return False
    
    NumberItems+=1
    QueueTail+=1
    if QueueTail==0:
        QueueHead=0
    Queue[QueueTail]=NewItem
    return True

def Dequeue():
    global Queue
    global QueueHead
    global QueueTail
    global NumberItems
    
    if NumberItems<1:
        return "False"
    NumberItems-=1
    QueueHead+=1
    return Queue[QueueHead-1]

def ReadData():
    try:
        f=open("BinaryData.txt",'r')
        for i in range(100):
            x=f.readline().strip()
            if x=="": break
            else: Enqueue(x)
                
        f.close()
    except IOError:
        print("File not found")
        
def Compress():
    global NewString
    NewString=""
    CurrentStr=""
    StopDequeue=False
    while not StopDequeue:
        Current=Dequeue()
        if Current=="False":
            StopDequeue=True
            NewString+=(CurrentStr[0]+str(len(CurrentStr)))
        else:
            if len(CurrentStr)==0:
                CurrentStr+=Current
            else:
                if Current==CurrentStr[0]:
                    CurrentStr+=Current
                else:
                    NewString+=(CurrentStr[0]+str(len(CurrentStr)))
                    CurrentStr=Current
            
                
    

#main
Queue=["" for _ in range(100)]
QueueHead=-1
QueueTail=-1
NumberItems=0

ReadData()
Compress()
print(NewString)
