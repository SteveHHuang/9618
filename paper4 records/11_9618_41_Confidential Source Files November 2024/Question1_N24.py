def ReadData():
    try:
        f=open("Data.txt", 'r')
        DataArray=[] # DECLARE: DataArray: ARRAY[0:44] OF STRING
        for item in f:
            DataArray.append(item.strip())
        f.close()
    except IOError:
        print("File not found.")
        
    return DataArray

def FormatArray(ArrOfString):
    Result=""
    for data in ArrOfString:
        Result+=data+' '
    Result=Result[0:len(Result)]
    return Result

def CompareStrings(Str1,Str2):
    Same=True
    Count=0
    Result=1
    while Same:
        if Str1[Count].lower()>Str2[Count].lower():
            Same=False
        elif Str1[Count].lower()<Str2[Count].lower():
            Same=False
            Result=2
        Count+=1
    return Result

def Bubble(ArrOfString):
    j=len(ArrOfString)
    Swapped=True
    while Swapped and j>0:
        Swapped=False
        for i in range(j-1):
            if CompareStrings(ArrOfString[i],ArrOfString[i+1])==1:
                temp=ArrOfString[i]
                ArrOfString[i]=ArrOfString[i+1]
                ArrOfString[i+1]=temp
                Swapped=True
        j-=1
        
        

#main
ArrayRead=ReadData()
ConcatenatedData=FormatArray(ArrayRead)
print(ConcatenatedData)
print("")
Bubble(ArrayRead)
ConcatenatedData1=FormatArray(ArrayRead)
print(f"Sorted: {ConcatenatedData1}")