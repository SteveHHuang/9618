NumberArray = [100,85,644,22,15,8,1] # 1D array with integer type



def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= -1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements-1)
        LastItem = IntegerArray[NumberElements-1]
        CheckItem = NumberElements -2
        
    LoopAgain = True
    
    if CheckItem <0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem: 
        LoopAgain = False
        
    while LoopAgain:
        IntegerArray[CheckItem+1] = IntegerArray[CheckItem]
        CheckItem -=1
        if CheckItem <0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem: 
            LoopAgain = False
        
    IntegerArray[CheckItem+1] = LastItem
    return IntegerArray


print("Recursive")
print(RecursiveInsertion(NumberArray, len(NumberArray)))

def IterativeInsertion(IntegerArray, NumberElements):
    if NumberElements <= -1:
        return IntegerArray
    
    for i in range(1, NumberElements):
        HolePosition = i
        temp = IntegerArray[HolePosition]
        while HolePosition > 0 and IntegerArray[HolePosition-1] > temp:
            IntegerArray[HolePosition] = IntegerArray[HolePosition-1]
            HolePosition -=1
        IntegerArray[HolePosition] = temp
    
    return IntegerArray

print("Iterative")
print(IterativeInsertion(NumberArray, len(NumberArray)))

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    mid = (First + Last)//2
    if IntegerArray[mid] == ToFind:
        return mid
    elif IntegerArray[mid] < ToFind:
        return BinarySearch(IntegerArray, mid+1, Last, ToFind)
    else:
        return BinarySearch(IntegerArray, First, mid-1, ToFind)

result = BinarySearch(IterativeInsertion(NumberArray, len(NumberArray)), 0, len(IterativeInsertion(NumberArray, len(NumberArray))), 644)    
if result == -1:
    print("Not Found")
else: 
    print(result)