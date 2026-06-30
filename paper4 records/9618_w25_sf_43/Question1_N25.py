class BoardObject:
    def __init__(self,c,v):
        self.__Code=c # PRIVATE Code: STRING
        self.__Value=v # PRIVATE Value: INTEGER
        
    def GetCode(self): return self.__Code
    def GetValue(self): return self.__Value

class Board:
    def __init__(self):
        self.__TheBoard=[[BoardObject("-",0) for _ in range(10)] for _ in range(10)] # PRIVATE TheBoard: ARRAY[0:9,0:9] OF BoardObject
    
    def GetObject(self,r,c): return self.__TheBoard[r][c]
    
    def SetObject(self,Obj,r,c): self.__TheBoard[r][c]=Obj
    
    def DisplayBoard(self):
        for row in self.__TheBoard:
            for Obj in row:
                print(Obj.GetCode(),end=" ")
            print("")
    
#main
Object1=BoardObject("A",2)
Object2=BoardObject("B",3)
Object3=BoardObject("C",5)
Object4=BoardObject("D",2)
Object5=BoardObject("E",7)

Board1=Board()
Board1.SetObject(Object1,0,0)
Board1.SetObject(Object2,9,9)
Board1.SetObject(Object3,4,5)
Board1.SetObject(Object4,2,2)
Board1.SetObject(Object5,8,7)
Board1.DisplayBoard()

InvalidRow=True
InvalidColumn=True
while InvalidRow:
    Row=int(input("Enter a row position between 0 and 9 inclusive. "))
    if Row>=0 and Row<=9: InvalidRow=False
    else: print("Invalid row position.")
while InvalidColumn:
    Column=int(input("Enter a column position between 0 and 9 inclusive. "))
    if Column>=0 and Column<=9: InvalidColumn=False
    else: print("Invalid column position.")
        
Object0=Board1.GetObject(Row,Column)
if Object0.GetCode()=="-": print("Miss")
else: print(f"Code: {Object0.GetCode()} Value: {Object0.GetValue()}")