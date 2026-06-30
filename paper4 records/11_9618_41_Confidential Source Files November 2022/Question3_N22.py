def SearchValue(Root,ValueToFind):
    global ArrayNodes
    if Root==-1: return -1
    elif ArrayNodes[Root][1]==ValueToFind: return Root
    elif ArrayNodes[Root][1]==-1: return -1
    
    if ArrayNodes[Root][1]>ValueToFind: return SearchValue(ArrayNodes[Root][0],ValueToFind)
    if ArrayNodes[Root][1]<ValueToFind: return SearchValue(ArrayNodes[Root][2],ValueToFind)

def PostOrder(Root):
    global ArrayNodes
    if ArrayNodes[Root][0] != -1: PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2] != -1: PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])


#main
ArrayNodes=[[-1,-1,-1] for _ in range(20)]
ArrayNodes[0]=[1,20,5]
ArrayNodes[1]=[2,15,-1]
ArrayNodes[2]=[-1,3,3]
ArrayNodes[3]=[-1,9,4]
ArrayNodes[4]=[-1,10,-1]
ArrayNodes[5]=[-1,58,-1]
FreeNode=6
RootPointer=0

if SearchValue(RootPointer,15)==-1: print("The value was not found.")
else: print(SearchValue(RootPointer,15))
print('')
PostOrder(RootPointer)