class Node:
    def __init__(self,data):
        self.LeftNode = None
        self.Data = data
        self.RightNode = None
        
node1 = Node(12)

node2 = Node(200)

node1.RightNode = node2

node3 = Node(10)

node1.LeftNode = node3

root = node1

def printBinTree_1(root):
    if root != None:
        printBinTree_1(root.LeftNode)
        print(root.Data)
        printBinTree_1(root.RightNode)
        
def addNode(data):
    global root
    #比当前node小或者等于node的数放左边，否则放右边。
    if root == None:
        root = Node(data)
        result = "Successfully added"
        return result
    ptr = root
    
    while ptr != None:

        if data > ptr.Data: 
            ptr = ptr.RightNode
        else: 
            ptr = ptr.LeftNode

    ptr = Node(data)
    result = "Successfully added"
    return result

addNode(200)

def searchTree(data,ptr):

    if ptr == None:
        return -1
    if data == ptr.Data:
        return ptr
    elif ptr.Data<data:
        return searchTree(data, ptr.RightNode)
    else:
        return searchTree(data, ptr.LeftNode)
    
searchTree(10,root)

def recursive_addNode(data,ptr):
    #比当前node小或者等于node的数放左边，否则放右边。
    if ptr == None:
        ptr = Node(data)
        return "Successfully added"
    elif ptr.Data<data:
        return recursive_addNode(data, ptr.RightNode)
    else:
        return recursive_addNode(data, ptr.LeftNode)
printBinTree_1(root)