# def AddNode():
#     global ArrayNodes, RootPointer, FreeNode
#     NodeData=int(input("Enter the data "))
#     if FreeNode<=19:
#         ArrayNodes[FreeNode][0]=-1
#         ArrayNodes[FreeNode][1]=NodeData
#         ArrayNodes[FreeNode][2]=-1
#         if RootPointer == -1:
#             RootPointer=0
#         else:
#             Placed=False
#             CurrentNode=RootPointer
#             while not Placed:
#                 if NodeData<ArrayNodes[CurrentNode][1]:
#                     if ArrayNodes[CurrentNode][0]==-1:
#                         ArrayNodes[CurrentNode][0]=FreeNode
#                         Placed=True
#                     else:
                        
#                         CurrentNode=ArrayNodes[CurrentNode][0]
#                 else:
#                     if ArrayNodes[CurrentNode][2]==-1:
#                         ArrayNodes[CurrentNode][2]=FreeNode
#                         Placed=True
#                     else:
#                         CurrentNode=ArrayNodes[CurrentNode][2]
#         FreeNode+=1
#     else:
#         print("Tree is full")
        
def AddNode(Root):
    global ArrayNodes, RootPointer, FreeNode
    NodeData=int(input("Enter the data "))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer == -1:
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
        print("Tree is full")        
        
def PrintAll():
    global ArrayNodes
    for item in ArrayNodes:
        if item[1] is not None:
            print(f"{item[0]}  {item[1]}  {item[2]}")

def InOrder(ptr):
    global ArrayNodes
    
    if ArrayNodes[ptr][1] is not None:
        InOrder(ArrayNodes[ptr][0])
        print(ArrayNodes[ptr][1])
        InOrder(ArrayNodes[ptr][2])
    
# ArrayNodes: ARRAY[0:2][0:19] OF INTEGER
# RootPointer: Integer
# FreeNode: Integer
ArrayNodes=[[-1,None,-1]for _ in range(20)] #改： DECLARE ArrayNodes: ARRAY [0:19,0:2] OF INTEGER
RootPointer=-1 #改： DECLARE RootPointer: INTEGER
FreeNode=0 #改: DECLARE FreeNode: Integer
for j in range(10):
    AddNode()
    
PrintAll()
InOrder(RootPointer)