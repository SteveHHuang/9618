# 20250925 
# 41s25 Q3
# OOP binary tree

#a
class Node:
    def __init__(self, data):
        self.__NodeData = data # Integer datatype,initialised to the parameter value, data stores the node’s integer data
        self.__LeftNode = None # Stores the node that is stored to the left of the current node, or a null value if there is no node to the left. Initialised to None
        self.__RightNode = None # Stores the node that is stored to the right of the current node, or a null value if there is no node to the right. Initialised to None
    

    def GetLeft(self):
        return self.__LeftNode

    def GetRight(self):
        return self.__RightNode
    
    def GetData(self):
        return self.__NodeData
    
    
    def SetLeft(self, Node):
        self.__LeftNode = Node
    
    def SetRight(self, Node):
        self.__RightNode = Node
 
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(5)
Node4 = Node(15)
Node5 = Node(7) 
        
class Tree:
    def __init__(self, Root): # Initialises FirstNode to its parameter value
        self.__FirstNode = Root # Stores the root node in the tree, initialised to the value of Root.
    def GetRootNode(self):
        return self.__FirstNode
    
    def Insert(self, Node):
        Root = self.GetRootNode()
        
        Found = False
        while not Found:
            
            if Node.GetData() > Root.GetData():
                if Root.GetRight() == None:
                    Root.SetRight(Node)
                    Found = True
                Root = Root.GetRight()
            else: 
                if Root.GetLeft() == None:
                    Root.SetLeft(Node)
                    Found = True
                Root = Root.GetLeft()

def OutputInOrder(Node):
    if Node is not None:
        OutputInOrder(Node.GetLeft())
        print(Node.GetData())
        OutputInOrder(Node.GetRight())


Tree1 = Tree(Node1)      
Tree1.Insert(Node2)
Tree1.Insert(Node3)
Tree1.Insert(Node4)
Tree1.Insert(Node5)


OutputInOrder(Node1)