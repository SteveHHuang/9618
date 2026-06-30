import random

# def Output():
#     for row in ArrayData:
#         temp=""
#         for co in row:
#             temp+=str(co)+' '
#         print(temp)
        
def Output():
    for row in ArrayData:
        for item in row:
            print(item, end=' ')
        print('')
        
def BinarySearch(SearchArray, Lower, Upper, SearchValue):

    if Upper>=Lower:
        Mid=(Lower+Upper)//2
        if SearchArray[0][Mid] == SearchValue: 
            return Mid
        else:
             if SearchArray[0][Mid] > SearchValue: 
                 return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
             else:
                return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)

    return -1

# main
ArrayData=[[random.randint(1,100)for _ in range(10)] for _ in range(10)]

Output()

ArrayLength=10
for x in range(0,ArrayLength):
    for y in range(0,ArrayLength-1):
        for z in range(0,ArrayLength-y-1):
            if ArrayData[x][z]>ArrayData[x][z+1]:
                TempValue=ArrayData[x][z]
                ArrayData[x][z]=ArrayData[x][z+1]
                ArrayData[x][z+1]=TempValue
print("-------------------------")
Output()
print("-------------------------")
print(BinarySearch(ArrayData, 0, 9, int(input("Enter the value you want to find out. "))))
print(BinarySearch(ArrayData, 0, 9, int(input("Enter the value you want to find out. "))))