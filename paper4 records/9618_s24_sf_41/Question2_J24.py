class Tree:
    def __init__(self,tn,hg,mh,mw,evg):
        self.__TreeName=tn # PRIVATE TreeName: STRING
        self.__HeightGrowth=hg # PRIVATE HeightGrowth: INTEGER
        self.__MaxHeight=mh # PRIVATE MaxHeight: INTEGER
        self.__MaxWidth=mw # PRIVATE MaxWidth: INTEGER
        self.__Evergreen=evg # PRIVATE Evergreen: STRING
        
    def GetTreeName(self): return self.__TreeName
    def GetHeightGrowth(self): return self.__HeightGrowth
    def GetMaxHeight(self): return self.__MaxHeight
    def GetMaxWidth(self): return self.__MaxWidth
    def GetEvergreen(self): return self.__Evergreen
    
def ReadData():
    try:
        fr=open("Trees.txt",'r')
        x=fr.readline().strip()
        ArrayTree=[]

        while x != "":
            x=x.split(',')
            ArrayTree.append(Tree(x[0],int(x[1]),int(x[2]),int(x[3]),x[4]))
            x=fr.readline().strip()
        
        fr.close()

    except IOError:
        print("File not found.")
    
    return ArrayTree

def PrintTrees(Tr):
    print(f"{Tr.GetTreeName()} has a maximum height {Tr.GetMaxHeight()} a maximum width {Tr.GetMaxWidth()} and grows {Tr.GetHeightGrowth()} cm a year.", end=" ")
    if Tr.GetEvergreen()=="No": print("It loses its leaves each year.")
    else: print("It does not lose its leaves.")
    
def ChooseTree(ArrayOfTree):
    mh=int(input("Enter the maximum height the tree can be in cm. "))
    mw=int(input("Enter the maximum width the tree can be in cm. "))
    evg=input("Do you expect the tree to be evergreen? Enter 'yes' or 'no'. ").lower()
    AvaliableTree=[]
    
    for EachTree in ArrayOfTree:
        if EachTree.GetMaxHeight()<=mh and EachTree.GetMaxWidth()<=mw and EachTree.GetEvergreen().lower()==evg:
            AvaliableTree.append(EachTree)
    
    if len(AvaliableTree)==0:
        print("There is no tree that meets your requirement.")
    else:
        for EachTree in AvaliableTree:
            PrintTrees(EachTree)
        WantedTree=input("Enter the name of one of the trees you want. ").lower()
        TreeHeight=int(input("Enter the current height of the tree you expect. "))
        for EachTree in AvaliableTree:
            if EachTree.GetTreeName().lower()==WantedTree:
                print(f"The tree will take {(EachTree.GetMaxHeight()-TreeHeight)//EachTree.GetHeightGrowth()} years to reach the maximum height {EachTree.GetMaxHeight()}cm.")
    
#main
Trees=ReadData()
PrintTrees(Trees[0])
ChooseTree(Trees)