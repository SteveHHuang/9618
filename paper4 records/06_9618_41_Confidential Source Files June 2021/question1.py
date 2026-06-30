class node:
    def __init__(self,data,nextNode):
        self.data=data
        self.nextNode=nextNode
        
def outputNodes(array):
    global startPointer
    ptr=startPointer
    while ptr!=-1:
        print(array[ptr].data)
        ptr=array[ptr].nextNode
        
def addNode():
    global linkedList,startPointer,emptyList
    
    if emptyList==-1:
        return False
    Data=int(input("Enter the data\n"))
    NewNodePtr=emptyList
    emptyList=linkedList[emptyList].nextNode
    
    linkedList[NewNodePtr].data=Data
    linkedList[NewNodePtr].nextNode=-1
    
    if startPointer ==-1:
        startPointer=NewNodePtr
    else:
        tempPtr=startPointer
        while tempPtr!=-1:
            ThisPtr=tempPtr
            tempPtr=linkedList[tempPtr].nextNode
        linkedList[ThisPtr].nextNode=NewNodePtr
        
    return True
            
    

if __name__ == "__main__":
    startPointer=0
    emptyList=5
    linkedList=[node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
    
    outputNodes(linkedList)
    if addNode():print("Successfully added.")
    else: print("List is full.")
    outputNodes(linkedList)