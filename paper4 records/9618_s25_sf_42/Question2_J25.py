class NewRecord:
    def __init__(self,k,i1,i2):
        self.Key=k # DECLARE Keys: INTEGER
        self.Item1=i1 # DECLARE Item1: INTEGER
        self.Item2=i2 # DECLARE Item2: INTEGER
        
global HashTable # DECLARE HashTable: ARRAY[0:199] OF NewRecord
global Spare # DECLARE Spare: ARRAY[0:99] OF NewRecord

def Initialise():
    global HashTable
    global Spare
    HashTable=[NewRecord(-1,-1,-1) for _ in range(200)]
    Spare=[NewRecord(-1,-1,-1) for _ in range(100)]

def CalculateHash(Key):
    return Key % 200 

def InsertIntoHash(New):
    global HashTable
    global Spare
    Index=CalculateHash(New.Key)
    if HashTable[Index].Key==-1:
        HashTable[Index]=New
    else:
        for j in range(100):
            if Spare[j].Key==-1:
                Spare[j]=New
                break
            
def CreateHashTable():
    try:
        f=open("HashData.txt",'r')
        x=f.readline().strip()
        while x!="":
            y=x.split(',')
            NewRec=NewRecord(int(y[0]),int(y[1]),int(y[2]))
            InsertIntoHash(NewRec)
            x=f.readline().strip()
        f.close()
    except IOError:
        print("File not found.")

def PrintSpare():
    global Spare
    for k in range(100):
        if Spare[k].Key==-1: break   
        else: print(Spare[k].Key)
    
    
#main
HashTable=[]
Spare=[]

Initialise()
CreateHashTable()
PrintSpare()
