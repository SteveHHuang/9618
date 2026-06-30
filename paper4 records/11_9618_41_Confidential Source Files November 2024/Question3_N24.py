global LinkedList # DECLARE LinkedList: ARRAY[0:19, 0:1] OF INTEGER
global FirstEmpty # DECLARE FirstEmpty: INTEGER
global FirstNode # DECLARE FirstNode: INTEGER

def InsertData():
    global LinkedList
    global FirstEmpty
    global FirstNode
    
    for j in range(5):
        Num=int(input("Enter a positive integer. "))
        
        if not FirstEmpty == -1:
            LinkedList[FirstEmpty][0]=Num
            temp=LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][1]=FirstNode
            FirstNode=FirstEmpty
            FirstEmpty=temp
        else:
            break

def OutputLinkedList():
    global LinkedList
    global FirstEmpty
    global FirstNode
    
    i=FirstNode
    while i!=-1:
        print(LinkedList[i][0])
        i=LinkedList[i][1]
        
def RemoveData(Num):
    global LinkedList
    global FirstEmpty
    global FirstNode
    
    Current=FirstNode
    while Current!=-1:
        if LinkedList[Current][0]==Num:
            if Current==FirstNode:
                FirstNode=LinkedList[Current][1]
            else:
                LinkedList[Last][1]=LinkedList[Current][1]
            LinkedList[Current][1]=FirstEmpty
            FirstEmpty=Current
            break
        else:
            Last=Current
            Current=LinkedList[Current][1]
        
        
#main
LinkedList=[[-1,i+1] for i in range(20)]
LinkedList[19][1]=-1
FirstEmpty=0
FirstNode=-1


InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()