#a
ArrayNodes = [[None for i in range(3)] for i in range(20)] # An 2D array stores nodes
RootPointer = -1 #ingeger datatype, initialised to -1, points to the first node in the binary tree
FreeNode = 0 #ingeger datatype, initialised to 0, points to the first empty node in the array
#b
def AddNode():
    global ArrayNodes, RootPointer, FreeNode
    NodeData = int(input("Enter the data.\n"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData <= ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
                        
        FreeNode += 1
        
        
    else:
        print("Tree is full")
#c        
def PrintAll():
    global ArrayNodes
    for i in range(len(ArrayNodes)):
        if ArrayNodes[i][1] !=None:
            print(f"{ArrayNodes[i][0]}  {ArrayNodes[i][1]}  {ArrayNodes[i][2]}")
        else: break
#d        
for i in range(10):
    AddNode()
    PrintAll()
    
#e
def InOrder(ptr):
    global ArrayNodes
    
    if ArrayNodes[ptr][1] != None:
        InOrder(ArrayNodes[ptr] [0])
        print(ArrayNodes[ptr][1])
        InOrder(ArrayNodes[ptr][2])

InOrder(RootPointer)