class Node:
    def __init__(self, TheData):
        self.__TheData = TheData # TheData is a private member with integer type, stores the data, TheData is initilised to the value of the parameter
        self.__NextNode = None # NextNode is a private member,stores the next node in the linked list, NextNode is initilised to a null value
        
    def GetData(self):
        return self.__TheData
        
    def GetNextNode(self):
        return self.__NextNode
    
    def SetNextNode(self, Node):
        self.__NextNode = Node
        
class LinkedList:
    def __init__(self):
        self.HeadNode = None # The first node in the linked list, initilised to a null value
        
    def InsertNode(self,num):
        NewNode = Node(num)
        NewNode.SetNextNode(self.HeadNode)
        
        self.HeadNode = NewNode
        
    def Traverse(self):
        ptr = self.HeadNode
        ResultStr = ""
        while ptr is not None:
            ResultStr+=str(ptr.GetData())
            ResultStr+=' '
            ptr = ptr.GetNextNode()
        return ResultStr
            
    def RemoveNode(self,num):
        if self.HeadNode is None:
            return False
        elif self.HeadNode.GetData() == num:
            self.HeadNode = self.HeadNode.GetNextNode()
            return True
        else:
            ptr = self.HeadNode.GetNextNode()
            while ptr is not None:
                
                if ptr.GetNextNode().GetData() == num:
                    temp = ptr.GetNextNode().GetNextNode()
                    ptr.SetNextNode(temp)
                    return True
                
                ptr = ptr.GetNextNode()
            return False

LinkedLST = LinkedList()
LinkedLST.InsertNode(10)
LinkedLST.InsertNode(20)
LinkedLST.InsertNode(30)
LinkedLST.InsertNode(40)
LinkedLST.InsertNode(50)
print(LinkedLST.Traverse())
LinkedLST.RemoveNode(30)
print(LinkedLST.Traverse())
