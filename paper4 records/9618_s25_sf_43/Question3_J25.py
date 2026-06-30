class Node:
    def __init__(self,td):
        self.__TheData=td # PRIVATE TheData: INTEGER
        self.__NextNode=None # PRIVATE NextNode: Node
        
    def GetData(self): return self.__TheData
    def GetNextNode(self): return self.__NextNode
    
    def SetNextNode(self,Next): self.__NextNode=Next
    
class LinkedList:
    def __init__(self):
        self.__HeadNode=None # PRIVATE HeadNode: Node
    
    def InsertNode(self,Num):
        NewNode=Node(Num)
        NewNode.SetNextNode(self.__HeadNode)
        self.__HeadNode=NewNode
    
    def Traverse(self):
        ResultString=""
        CurrentNode=self.__HeadNode
        while CurrentNode is not None:
            ResultString+=str(CurrentNode.GetData())+" "
            CurrentNode=CurrentNode.GetNextNode()
        
        return ResultString[0:len(ResultString)]
    
    def RemoveNode(self,Num):
        if self.__HeadNode is None:
            return False
        
        if self.__HeadNode.GetData()==Num:
            self.__HeadNode=self.__HeadNode.GetNextNode()
            return True
        else:
            CurrentNode=self.__HeadNode
            LastNode=self.__HeadNode
            while CurrentNode is not None:
                if CurrentNode.GetData()==Num:
                    LastNode.SetNextNode(CurrentNode.GetNextNode())
                    return True
                else:
                    LastNode=CurrentNode
                    CurrentNode=CurrentNode.GetNextNode()
        return False
    
#main
LList=LinkedList()
LList.InsertNode(10)
LList.InsertNode(20)
LList.InsertNode(30)
LList.InsertNode(40)
LList.InsertNode(50)

print(LList.Traverse())
LList.RemoveNode(30)
print(LList.Traverse())