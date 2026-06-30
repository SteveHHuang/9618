def AddNode():
    global ArrayNodes,RootPointer,FreeNode
    NodeData=int(input("Enter the data.\n"))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=0
        else:
            Placed=False
            CurrentNode=RootPointer
            while not Placed:
                if NodeData<ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2]==-1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode+=1
    else:
        print("Tree is full.")
     
def PrintAll():
    global ArrayNodes
    for node in ArrayNodes:
        if node[1] is not None:
            print(f"{node[0]}  {node[1]}  {node[2]}")
        else:continue
def InOrder(root):
    global ArrayNodes
    if ArrayNodes[root][1] is not None:
        InOrder(ArrayNodes[root][0])
        print(ArrayNodes[root][1])
        InOrder(ArrayNodes[root][2])
                   
            
if __name__ =="__main__":
    ArrayNodes=[[-1,None,-1] for _ in range(20)]
    RootPointer=-1
    FreeNode=0
    for i in range(10):
        AddNode()
    
    PrintAll()
    InOrder(0)