class SaleData:
    def __init__(self,id,quant):
        self.ID=id
        self.Quantity=quant
        
def Enqueue(New):
    global Head,Tail,NumberOfItems
    global CircularQueue
    if NumberOfItems >= len(CircularQueue):
        return -1
    CircularQueue[Tail]=New
    Tail+=1
    if Tail >=len(CircularQueue):
        Tail=0
    NumberOfItems+=1
    return 1

def Dequeue():
    global Head,Tail,NumberOfItems
    global CircularQueue
    if NumberOfItems==0:
        return SaleData("",-1)
    DataToReturn=CircularQueue[Head]
    Head+=1
    if Head >= len(CircularQueue):
        Head=0
    NumberOfItems-=1
    return DataToReturn

def EnterRecord():
    id=input("Enter the ID of the new sale record. ")
    q=int(input("Enter the quantity of the new sale record. "))
    NewSaleRecord=SaleData(id,q)
    Status=Enqueue(NewSaleRecord)
    if Status==1: print("Stored")
    else: print("Full")         

#main
CircularQueue=[SaleData("",-1) for _ in range(5)]
Head=0
Tail=0
NumberOfItems=0
for i in range(6):
    EnterRecord()
sd=Dequeue()
if sd.ID=="": print("The circular queue is empty")
else: print(f"ID: {sd.ID}, Quantity: {sd.Quantity}")
EnterRecord()

for item in CircularQueue:
    print(f"ID: {item.ID}, Quantity: {item.Quantity}")