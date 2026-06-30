def PrintArray(IntegerArray):
    for item in IntegerArray:
        print(item, end=' ')
    print("")

def LinearSearch(IntegerArray, num):
    count=0
    for item in IntegerArray:
        if num==item:
            count+=1
            
    return count


# main

DataArray=[-1 for _ in range(25)]

frdata=open("Data.txt",'r')
for i in range(25):
    DataArray[i]=int(frdata.readline().strip())
frdata.close()    
    
PrintArray(DataArray)

Valid=False
while not Valid:
    InputNum=int(input("Enter a number between 0 and 100 inclusive. "))
    if InputNum>=0 and InputNum<=100:
        Valid=True
    else:
        print("Invalid number.")
Counted=LinearSearch(DataArray,InputNum)
print(f"The number {InputNum} is found {Counted} times.")