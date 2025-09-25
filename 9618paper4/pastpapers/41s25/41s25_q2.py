#20250924

#a
def ReadData():
    name = input("Enter the name of the file\n")
    arr = [] # it will be returned
    try:
        f = open(name, "r")
        for i in range(72):
            temp = f.readline()
            
            if temp is None:
                continue
            arr.append(temp.strip())
        f.close()
        return arr
    except:
        print("error")

#b
def SplitData(DataArray):
    red = []
    green = []
    blue =[]
    orange = []
    yellow = []
    pink = []
    
    for i in range(72):
        temp = DataArray[i]
        temparr = temp.split(',')
        if temparr[1] == "red":
            red.append(int(temparr[0]))
        elif temparr[1] == "green":
            green.append(int(temparr[0]))
        elif temparr[1] == "blue":
            blue.append(int(temparr[0]))
        elif temparr[1] == "orange":
            orange.append(int(temparr[0]))
        elif temparr[1] == "yellow":
            yellow.append(int(temparr[0]))
        elif temparr[1] == "pink":
            pink.append(int(temparr[0]))


#c        
def StoreData(DataToStore, name):
    try:
        f = open(name, "a")
        for i in range(len(DataToStore)):
            print(DataToStore[i])
            if DataToStore[i] is None:
                continue
            f.write(str(DataToStore[i])+'\n')
            
        
        f.close()
    except:
        print("error")
#d    
def SplitData(DataArray):
    red = []
    green = []
    blue =[]
    orange = []
    yellow = []
    pink = []
    
    for i in range(72):
        temp = DataArray[i]
        temparr = temp.split(',')
        if temparr[1] == "red":
            red.append(int(temparr[0]))
        elif temparr[1] == "green":
            green.append(int(temparr[0]))
            
        elif temparr[1] == "blue":
            blue.append(int(temparr[0]))
        elif temparr[1] == "orange":
            orange.append(int(temparr[0]))
            
        elif temparr[1] == "yellow":
            yellow.append(int(temparr[0]))
        elif temparr[1] == "pink":
            pink.append(int(temparr[0]))
        
    StoreData(red, "Red.txt")
    StoreData(green, "Green.txt")
    StoreData(blue, "Blue.txt")
    StoreData(orange, "Orange.txt")
    StoreData(yellow, "Yellow.txt")
    StoreData(pink, "Pink.txt")


arr = ReadData()

SplitData(arr)