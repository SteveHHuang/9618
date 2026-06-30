class RecordData:
    def __init__(self,id,t):
        self.ID=id #DECLARE ID: STRING
        self.Total=t #DECLARE Total: INTEGER

def Enqueue(New):
    global Queue
    global HeadPointer,TailPointer
    if TailPointer>=len(Queue):
        print("The queue is full.")
    else:
        Queue[TailPointer]=New
        TailPointer+=1
        if HeadPointer < 0:
            HeadPointer=0

def Dequeue():
    global Queue
    global HeadPointer,TailPointer
    if TailPointer-HeadPointer<=0:
        print("The queue is empty.")
        return "Empty"
    DataToReturn=Queue[HeadPointer]
    HeadPointer+=1
    return DataToReturn
    
def ReadData():
    fr=open("QueueData.txt",'r')
    
    for item in fr:
        Enqueue(item.strip())
    
    fr.close()

def TotalData():
    global Records
    global NumberRecords
    DataAccessed=Dequeue()
    Flag=False
    if NumberRecords==0:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        Flag=True
        NumberRecords+=1
    else:
        for x in range(NumberRecords):
            if Records[x].ID==DataAccessed:
                Records[x].Total+=1
                Flag=True
    if Flag==False:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        NumberRecords+=1

def OutputRecords():
    global Records
    global NumberRecords
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID}  Total {Records[i].Total}")


#main
Queue=["" for _ in range(50)]
HeadPointer=-1
TailPointer=0
Records=[RecordData("", -1) for _ in range(50)]
NumberRecords=0

ReadData()
for i in range(HeadPointer,TailPointer):
    TotalData()
OutputRecords()
