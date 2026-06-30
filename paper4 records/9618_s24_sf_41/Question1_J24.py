def Initialise():
    global DataStored
    global NumberItems
    
    Valid=False
    while not Valid:
        Quantity=int(input("Enter the number of quantity of the numbers, between 1 and 20 inclusive. "))
        if Quantity>=1 and Quantity<=20:
            NumberItems=Quantity
            Valid=True
        else:
            print("Invalid number input.")
        
    for i in range(NumberItems):
        DataStored.append(int(input("Enter the number. ")))

def BubbleSort():
    global DataStored
    global NumberItems
    
    Sorted=False
    x=NumberItems
    while not Sorted or x>=0:
        Sorted=True
        for i in range(x-1):
           if DataStored[i]>DataStored[i+1]:
            temp=DataStored[i+1]
            DataStored[i+1]=DataStored[i]
            DataStored[i]=temp
            Sorted=False
        x-=1

def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    
    lower=0
    upper=NumberItems-1

    while lower<=upper:
        mid=(lower+upper)//2
        if DataStored[mid]==DataToFind:
            return mid
        elif DataStored[mid]>DataToFind:
            upper=mid-1
        else:
            lower=mid+1
    
    return -1         
    


#main
DataStored=[] # DECLARE DataStored: ARRAY[0:19] OF INTEGER
NumberItems=0
Initialise()
print(DataStored)
BubbleSort()
print(f"Sorted: {DataStored}")

print(BinarySearch(int(input("Enter a number you want to find. "))))