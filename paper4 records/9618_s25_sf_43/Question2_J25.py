def InsertionSort(ArrayInt):
    for i in range(1,len(ArrayInt)):
        HolePosition=i
        Data=ArrayInt[i]
        while HolePosition>0 and ArrayInt[HolePosition-1]>Data:
            ArrayInt[HolePosition]=ArrayInt[HolePosition-1]
            HolePosition-=1
        ArrayInt[HolePosition]=Data
    
    return ArrayInt

def OutputArray(ArrayInt):
    for Item in ArrayInt:
        print(Item, end=" ")
    print("")

def Search(DataArray,ItemToFind):
    Lower=0
    Upper=len(DataArray)-1
    
    while Upper>=Lower:
        Mid=(Lower+Upper)//2
        if DataArray[Mid]==ItemToFind:
            return Mid
        elif DataArray[Mid]>ItemToFind:
            Upper=Mid-1
        elif DataArray[Mid]<ItemToFind:
            Lower=Mid+1
    
    return -1
    


#main
DataArray=[0,3,4,56,67,44,43,32,31,345,45,6,54,1]

OutputArray(DataArray)
DataArray=InsertionSort(DataArray)
OutputArray(DataArray)

if Search(DataArray,0)==-1: print("0 was not found")
else: print(f"0 is in the index {Search(DataArray,0)}")
if Search(DataArray,345)==-1: print("345 was not found")
else: print(f"345 is in the index {Search(DataArray,345)}")
if Search(DataArray,67)==-1: print("67 was not found")
else: print(f"67 is in the index {Search(DataArray,67)}")
if Search(DataArray,2)==-1: print("2 was not found")
else: print(f"2 is in the index {Search(DataArray,2)}")