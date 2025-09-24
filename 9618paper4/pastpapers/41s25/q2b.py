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
