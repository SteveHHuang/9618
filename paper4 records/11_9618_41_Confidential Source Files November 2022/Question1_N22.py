def ReadFile():
    global DataArray
    try:
        fr=open("IntegerData.txt", 'r')
        for i in range(100):
            DataArray[i]=int(fr.readline().strip())
        fr.close()
    except IOError:
        print("File Not Found")

def FindValues():
    global DataArray
    InvalidNum = True
    while InvalidNum:
        TargetNum=int(input("Enter the number(between 1 and 100 inclusive) you want to find."))
        if TargetNum>=1 and TargetNum<=100: InvalidNum=False
    count=0
    for num in DataArray:
        if num==TargetNum:
            count+=1
    return count

def BubbleSort():
    global DataArray
    Counter=len(DataArray)
    while True:
        Sorted=False
        for i in range(Counter-1):
            if DataArray[i]>DataArray[i+1]:
                temp=DataArray[i]
                DataArray[i]=DataArray[i+1]
                DataArray[i+1]=temp
                Sorted=True
        Counter-=1
        if Sorted==False or Counter==0: break
    print(DataArray)

#main
DataArray=[-1 for _ in range(100)]
ReadFile()
NumAppeared=FindValues()
if NumAppeared == 0: print("The number does not appeared.")
else: print(f"The number appeared for {NumAppeared} times.") 
BubbleSort()                                                   