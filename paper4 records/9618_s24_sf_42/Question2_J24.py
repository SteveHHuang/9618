class Node:
    def __init__(self,data):
        self.__Data=data # PRIVATE Data: INTEGER
        self.__LeftPointer=-1 # PRIVATE LeftPointer: INTEGER
        self.__RightPointer=-1 # PRIVATE RightPointer: INTEGER
        
    def GetLeft(self): return self.__LeftPointer
    def GetRight(self): return self.__RightPointer
    def GetData(self): return self.__Data
    
    def SetLeft(self,num): self.__LeftPointer=num
    def SetRight(self,num): self.__RightPointer=num
    def SetData(self,num): self.__Data=num
    
class TreeClass:
    def __init__(self):
        self.__Tree=[Node(-1) for _ in range(19)] # PRIVATE Tree: ARRAY[0:19] OF Node
        self.__FirstNode=-1 # PRIVATE FirstNode: INTEGER
        self.__NumberNodes=0 # PRIVATE NumberNodes: INTEGER
        
    def InsertTree(self, NewNode):
        if self.__NumberNodes==0:
            self.__Tree[self.__NumberNodes]=NewNode
            self.__NumberNodes+=1
            self.__FirstNode=0
        else:
            self.__Tree[self.__NumberNodes]=NewNode
            Current=self.__FirstNode
            Found=False
            while not Found:
                if NewNode.GetData()>self.__Tree[Current].GetData():
                    if self.__Tree[Current].GetRight() == -1:
                        self.__Tree[Current].SetRight(self.__NumberNodes)
                        self.__NumberNodes+=1
                        Found=True
                    else:
                        Current=self.__Tree[Current].GetRight()
                else:
                    if self.__Tree[Current].GetLeft() == -1:
                        self.__Tree[Current].SetLeft(self.__NumberNodes)
                        self.__NumberNodes+=1
                        Found=True
                    else:
                        Current=self.__Tree[Current].GetLeft()
                        
    def OutputTree(self):
        if self.__NumberNodes==0:
            print("No nodes.")
        else:
            for i in range(self.__NumberNodes):
                print(f"{self.__Tree[i].GetLeft()} {self.__Tree[i].GetData()} {self.__Tree[i].GetRight()}")
                
#main
TheTree=TreeClass()
TheTree.InsertTree(Node(10))
TheTree.InsertTree(Node(11))
TheTree.InsertTree(Node(5))
TheTree.InsertTree(Node(1))
TheTree.InsertTree(Node(20))
TheTree.InsertTree(Node(7))
TheTree.InsertTree(Node(15))
TheTree.OutputTree()