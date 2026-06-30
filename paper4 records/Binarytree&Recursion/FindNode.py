def FindLeaves(CurrentNode):
 global BinaryTree
 if(BinaryTree[CurrentNode].LeftPointer != -1):
    FindLeaves(BinaryTree[CurrentNode].LeftPointer)
 if(BinaryTree[CurrentNode].RightPointer != -1):
    FindLeaves(BinaryTree[CurrentNode].RightPointer)
 if((BinaryTree[CurrentNode].RightPointer == -1) and (BinaryTree[CurrentNode].LeftPointer == -1)):
    print(BinaryTree[CurrentNode].DataValue)
