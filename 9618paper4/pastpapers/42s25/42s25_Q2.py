class NewRecord:
    def __init__(self,key, Item1, Item2):
        self.Key = key
        self.Item1 = Item1
        self.Item2 = Item2
        
HashTable = [None for i in range(200)] # an global 1D array with size 200 elements, type of NewRecord
Spare = [None for i in range(100)] # an global 1D array with size 100 elements, type of NewRecord

def Initialise():
    global HashTable, Spare
    for i in range(200):
        HashTable[i] = NewRecord(-1,-1,-1)
        if i <100:
            Spare[i] = NewRecord(-1,-1,-1)
            
def CalculateHash(Key):
    return Key%200

def InsertIntoHash(data):
    global HashTable, Spare
    index = CalculateHash(data.Key)
    if HashTable[index].Key != -1:
        for i in range(100):
            if Spare[i].Key == -1 and (Spare[i].Item1 == -1 and Spare[i].Item2 == -1):
                Spare[i].Key = data.Key
                Spare[i].Item1 = data.Item1
                Spare[i].Item2 = data.Item2
                break 
    else:
        HashTable[index].Key = data.Key
        HashTable[index].Item1 = data.Item1
        HashTable[index].Item2 = data.Item2
        
def CreateHashTable():
    f = open("HashData.txt", 'r')
    for i in range(200):
        temp = f.readline().strip()
        if temp == '': continue
        temparr = temp.split(",")
        tempRec = NewRecord(int(temparr[0]), int(temparr[1]), int(temparr[2]))
        InsertIntoHash(tempRec)
        
def PrintSpare():
    global Spare
    for i in range(100):
        if Spare[i].Key == -1 and (Spare[i].Item1 == -1 and Spare[i].Item2 == -1): break
        else: print(Spare[i].Key)
            
        
Initialise()
CreateHashTable()
PrintSpare()

    


    