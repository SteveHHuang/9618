class Node:
    def __init__(self,nd):
        self.__NodeData=nd # PRIVATE NodeData: INTEGER
        self.__LeftNode=None # PRIVATE LeftNode: INTEGER
        self.__RightNode=None # PRIVATE RightNode: INTEGER
    
    def GetLeft(self): return self.__LeftNode
    def GetRight(self): return self.__RightNode
    def GetData(self): return self.__NodeData
    
    def SetLeft(self,node): self.__LeftNode=node
    def SetRight(self,node): self.__RightNode=node

class Tree:
    def __init__(self,fn):
        self.__FirstNode=fn # PRIVATE FirstNode: Node
    
    def GetRootNode(self): return self.__FirstNode
    
    def Insert(self,NewNode):
        Current=self.GetRootNode()
        Found=False
        while not Found:
            if NewNode.GetData()<Current.GetData():
                if Current.GetLeft() is None:
                    Current.SetLeft(NewNode)
                    Found=True
                else:
                    Current=Current.GetLeft()
            else:
                if Current.GetRight() is None:
                    Current.SetRight(NewNode)
                    Found=True
                else:
                    Current=Current.GetRight()
        
def OutputInOrder(ANode):
    if ANode.GetLeft() is not None: OutputInOrder(ANode.GetLeft())
    print((ANode.GetData()))
    if ANode.GetRight() is not None: OutputInOrder(ANode.GetRight())

#main
Node1=Node(10)
Node2=Node(20)
Node3=Node(5)
Node4=Node(15)
Node5=Node(7)

Tree1=Tree(Node1)
Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)
OutputInOrder(Tree1.GetRootNode())