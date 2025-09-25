DataArray = [0,3,4,56,67,44,43,32,31,345,45,6,54,1]# 1D array with 14 elements

def InsertionSort(arr):
    k = len(arr)
    
    for i in range(1,k):
        temp = arr[i]
        HolePosition = i
        while arr[HolePosition-1] > temp and HolePosition>0:
            arr[HolePosition] = arr[HolePosition-1]
            HolePosition-=1
        arr[HolePosition] = temp

def OutputArray(arr):
    ResultStr = ""
    for i in range(len(arr)):
        ResultStr+=str(arr[i])
        if i < len(arr)-1:
            ResultStr+=" "
            
    print(ResultStr)
            
OutputArray(DataArray)
InsertionSort(DataArray)
OutputArray(DataArray)

def Search(DataArray, ItemToFind):
    lower = 0
    upper = len(DataArray)-1
    while lower<=upper:
        mid = (lower+upper)//2
        if DataArray[mid] == ItemToFind:
            return mid
        elif DataArray[mid] < ItemToFind:
            lower = mid+1
        else:
            upper = mid-1
            
    return -1

Targets = [0,345,67,2]
for num in Targets:
    result = Search(DataArray,num)
    if result == -1:
        print("The number was not found.")
    else: print(f"The number is in the index of {result}.")