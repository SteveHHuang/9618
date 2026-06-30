def RecursiveInsertion(IntegerArray,NumberElements):

    if NumberElements<=1: 
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray,NumberElements-1)
        LastItem=IntegerArray[NumberElements-1]
        CheckItem=NumberElements-2
    LoopAgain=True
    if CheckItem<0:
        LoopAgain=False
    elif IntegerArray[CheckItem]<LastItem:
        LoopAgain=False
    while LoopAgain:
        IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
        CheckItem-=1
        if CheckItem<0:
            LoopAgain=False
        elif IntegerArray[CheckItem]<LastItem:
            LoopAgain=False

    IntegerArray[CheckItem+1]=LastItem
    print(f"{IntegerArray},{NumberElements},{LastItem}")
    return IntegerArray

def IterativeInsertion(IntegerArray,NumberElements):
    
    for i in range(NumberElements):
        HolePosition=i
        Num=IntegerArray[i]
        while HolePosition>0 and IntegerArray[HolePosition-1] > Num:
            IntegerArray[HolePosition]=IntegerArray[HolePosition-1]
            HolePosition-=1
        Num=IntegerArray[HolePosition]
    return IntegerArray
        
def BinarySearch(IntegerArray,First,Last,ToFind):
    if First>Last:
        return -1
    
    Mid=(First+Last)//2
    if IntegerArray[Mid]==ToFind:
        return Mid
    elif IntegerArray[Mid]>ToFind:
        return BinarySearch(IntegerArray,First,Mid-1,ToFind)
    elif IntegerArray[Mid]<ToFind:
        return BinarySearch(IntegerArray,Mid+1,Last,ToFind)

    
#main
NumberArray=[100,85,644,22,15,8,1]

SortedArray=RecursiveInsertion(NumberArray, len(NumberArray))
print("Recursive")
print(SortedArray)

IterativeSortedArray=IterativeInsertion(NumberArray, len(NumberArray))
print("Iterative")
print(IterativeSortedArray)

Location=BinarySearch(IterativeSortedArray,0,len(IterativeSortedArray)-1,644)
if Location == -1: print("Not found")
else: print(Location)