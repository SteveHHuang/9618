def RecursiveCount(ArrayCopy,NumberElements,DataTofind):
    if NumberElements==0: 
        return 0
    if ArrayCopy[0]==DataTofind: 
        return RecursiveCount(ArrayCopy[1:len(ArrayCopy)],NumberElements-1,DataTofind)+1
    else: 
        return RecursiveCount(ArrayCopy[1:len(ArrayCopy)],NumberElements-1,DataTofind)
    
def SplitData(Data):
    Process=[]
    Task=""
    for char in Data:
        if char==";":
            Process.append(Task)
            Task=""
        else:
            Task+=char
    return Process

#main
DataArr=[0,5,1,2,5,9,9,6,5,0]
print(RecursiveCount(DataArr,10,0))

Processes="x=0;y=1;x=x+y;y++;"

ProcessArr=SplitData(Processes)
for Statement in ProcessArr:
    print(Statement)