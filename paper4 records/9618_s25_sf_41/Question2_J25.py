def ReadData():
    try:
        Name=input("Enter a file name. ")
        f=open(Name,'r')
        x=f.readline().strip()
        Array=[]
        while x!="":
            Array.append(x)
            x=f.readline().strip()
        f.close()
        return Array
    except IOError:
        print("File not found")
        
def SplitData(DataArray):
    Red=[]
    Green=[]
    Blue=[]
    Orange=[]
    Yellow=[]
    Pink=[]
    for Data in DataArray:
        Item=Data.split(',')
        if Item[1].lower()=="red":
            Red.append(int(Item[0]))
        elif Item[1].lower()=="green":
            Green.append(int(Item[0]))
        elif Item[1].lower()=="blue":
            Blue.append(int(Item[0]))
        elif Item[1].lower()=="orange":
            Orange.append(int(Item[0]))
        elif Item[1].lower()=="yellow":
            Yellow.append(int(Item[0]))
        elif Item[1].lower()=="pink":
            Pink.append(int(Item[0]))
            
    StoreData(Red,"Red.txt")
    StoreData(Green,"Green.txt")
    StoreData(Blue,"Blue.txt")
    StoreData(Orange,"Orange.txt")
    StoreData(Yellow,"Yellow.txt")
    StoreData(Pink,"Pink.txt")
    

def StoreData(DataToStore,FileName):
    try:
        fw=open(FileName,'a')
        for item in DataToStore:
            fw.write(str(item)+'\n')
        
        fw.close()
    except IOError:
        print("File not found or cannot be written")
        
#main
DataItems=ReadData()
SplitData(DataItems)
