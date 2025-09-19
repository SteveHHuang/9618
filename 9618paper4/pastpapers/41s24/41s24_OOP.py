class Tree:
    def __init__(self,TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen):
        self.__TreeName = TreeName # self.__TreeName is STRING
        self.__HeightGrowth = HeightGrowth # self.__HeightGrowth is INTEGER
        self.__MaxHeight = MaxHeight # self.__MaxHeight is INTEGER
        self.__MaxWidth = MaxWidth # self.__MaxWidth is INTEGER
        self.__Evergreen = Evergreen # self.__Evergreen is STRING
    
    def getTreeName(self):
        return self.__TreeName
    
    def getHeightGrowth(self):
        return self.__HeightGrowth
    
    def getMaxHeight(self):
        return self.__MaxHeight
    
    def getMaxWidth(self):
        return self.__MaxWidth
    
    def getEvergreen(self):
        return self.__Evergreen
    

def ReadData(filename):
    Trees = []
    try:
        f = open(filename, "r")
        for i in range(9):
            temp = f.readline()
            temp1 = temp.strip().split(",")
            Name = Tree(temp1[0], int(temp1[1]), int(temp1[2]), int(temp1[3]), temp1[4])
            Trees.append(Name)
        f.close()
        return Trees
        
    except: print("File not found.")
    

def PrintTrees(NameOfTree):
    if NameOfTree.getEvergreen() == "Yes":
        print(f"{NameOfTree.getTreeName()} has a maximum height {NameOfTree.getMaxHeight()}  a maximum width {NameOfTree.getMaxWidth()} and grows {NameOfTree.getHeightGrowth()} cm a year. It does not lose its leaves.")
    else: print(f"{NameOfTree.getTreeName()} has a maximum height {NameOfTree.getMaxHeight()}  a maximum width {NameOfTree.getMaxWidth()} and grows {NameOfTree.getHeightGrowth()} cm a year. It loses its leaves each year.")

temp = ReadData("/Users/hehuang/Documents/GitHub/9618/9618paper4/pastpapers/41s24/Trees.txt") # temp stores the returned array
PrintTrees(temp[0])


def ChooseTrees(Array):
    MatchedTrees = [] # Stores all the trees that meet the user's requirements 
    AcceptableMaxHeight = int(input("Enter the maximum height of the tree you want.\n"))
    AcceptableMaxWidth = int(input("Enter the maximum width of the tree you want.\n"))
    AcceptEvergreen = input("Do you want the tree keeps its leaves or loses its leaves? Enter Yes or No ONLY, otherwise you need to re-enter\n")
    while AcceptEvergreen !="Yes" and AcceptEvergreen !="No":
        AcceptEvergreen = input("Do you want the tree keeps its leaves or loses its leaves? Enter Yes or No ONLY, otherwise you need to re-enter\n")

    for i in range(len(Array)):
        if Array[i].getMaxHeight() <= AcceptableMaxHeight and Array[i].getMaxWidth() <= AcceptableMaxWidth and Array[i].getEvergreen() == AcceptEvergreen:
            MatchedTrees.append(Array[i])
            PrintTrees(Array[i])
    
    if len(MatchedTrees) == 0:
        print("There are no trees meet all your requirements")
    else:
        Cart = input("Enter the name of the tree you want to buy\n")
        
        TargetHeight = int(input("Enter the height of the tree in cm when it is bought\n"))
        for i in range(len(Array)):
            if Cart == Array[i].getTreeName():
                TargetPlace = i
            
        k = (Array[TargetPlace].getMaxHeight() - TargetHeight) / Array[TargetPlace].getHeightGrowth()
        if k - (Array[TargetPlace].getMaxHeight() - TargetHeight) // Array[TargetPlace].getHeightGrowth() !=0:
            result = int(k) +1
        else: result = k
        
        print(f"The tree will take {result} years to reach its maximum height of {Array[TargetPlace].getMaxHeight()}.")
        
print(temp)
ChooseTrees(temp)