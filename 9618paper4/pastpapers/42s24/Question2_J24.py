class Node:
    def __init__(self, Data):
        self.__LeftPointer = -1 # Integer type property, stores the index of the node to the left in the binary tree, initialised to -1
        self.__Data = Data # Integer type property, stores the node’s data, initalised to the parameter value
        self.__RightPointer = -1 # Integer type property, stores the index of the node to the right in the binary tree, initialised to -1
        
    def GetLeft(self):
        return self.__LeftPointer
    def GetRight(self):
        return self.__RightPointer
    def GetData(self):
        return self.__Data
    
    def SetLeft(self, Node):
        self.__LeftPointer = Node
    def SetRight(self, Node):
        self.__RightPointer = Node
    def SetData(self, Data):
        self.__Data = Data
    
class TreeNode:
    def __init__(self):
        self.Tree = [Node(-1) for i in range (20)] # an 1D array of 20 elements of type Node, each of the elements in Tree are initialised to a Node object with the data value of −1
        self.FirstNode = -1 # an integer property whic stores the index of the first node in the tree, initialised to -1
        self.NumberNodes = 0 # an integer type property which stores the quantity of nodes in the tree, initalised to 0
    def InsertNode(self, NewNode):
        if self.FirstNode == -1:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            self.Tree[self.NumberNodes] = NewNode
            ptr = self.Tree[self.FirstNode]
            Found = False
            while not Found:
                if NewNode.GetData() > ptr.GetData():
                    if ptr.GetRight() == -1:
                        ptr.SetRight(NewNode)
                        self.NumberNodes += 1
                        Found = True
                    ptr = ptr.GetRight()
                else:
                    if ptr.GetLeft() == -1:
                        ptr.SetLeft(NewNode)
                        self.NumberNodes += 1
                        Found = True
                    ptr = ptr.GetLeft()
    
    def OutputTree(self):
        if self.NumberNodes <1:
            print("No nodes.")
        else:
            for i in range(len(self.Tree)):
                if self.Tree[i].GetData() != -1:
                    print(self.Tree[i].GetLeft())
                    print(self.Tree[i].GetData())
                    print(self.Tree[i].GetRight())
                    
TheTree = TreeNode()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()