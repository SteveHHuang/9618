class Record:
    def __init__(self,k,d):
        self.Key=k
        self.Data=d
        
def InitialiseHashTable():
    global HashTable
    for x in range(len(HashTable)):
        for y in range(len(HashTable[x])):
            HashTable[x][y]=Record(-1,"")  
            
def Hash(Key):  
    return Key%100

def InsertData(Rec):
    global HashTable
    Position=Hash(Rec.Key)
    for i in range(len(HashTable[Position])):
        if HashTable[Position][i].Key==-1:
            HashTable[Position][i]=Rec
            break
        
def ReadData():
    fr=open("HashTableData.txt",'r')
    x=fr.readline()
    
    while x !="":
        DataRead=x.split(',')
        Key1=int(DataRead[0].strip())
        Data1=DataRead[1].strip()
        InsertData(Record(Key1,Data1))
        x=fr.readline()
        
    fr.close()
    
def GetRecord(Key):
    Location=Hash(Key)
    for i in range(len(HashTable[Location])):
        if HashTable[Location][i].Key==Key:
            return HashTable[Location][i].Data
        
    return "Not found"
            
    

#main
HashTable=[[None for _ in range(10)] for _ in range(100)]

InitialiseHashTable()
ReadData()

for i in range(5):
    KeyValue=int(input("Enter the key field value. "))
    print(GetRecord(KeyValue))