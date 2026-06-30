class Character:
    def __init__(self,n,x,y):
        self.__Name=n #PRIVATE Name:STRING
        self.__XCoordinate=x #PRIVATE Name:INTEGER
        self.__YCoordinate=y #PRIVATE Name:INTEGER
        
    def GetName(self): return self.__Name
    def GetXCoordinate(self): return self.__XCoordinate
    def GetYCoordinate(self): return self.__YCoordinate
    
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate+=XChange
        self.__YCoordinate+=YChange
        


#main
Characters=[Character("",-1,-1) for _ in range(10)]
fr=open("Characters.txt", 'r')

for i in range(10):
    Name=fr.readline().strip()
    Xcor=int(fr.readline().strip())
    Ycor=int(fr.readline().strip())
    Characters[i]=Character(Name,Xcor,Ycor)

fr.close()

Position=-1
Found = False
while not Found:
    NameToFind=input("Enter the name of the character.")
    for i in range(10):
        if Characters[i].GetName()==NameToFind:
            Position=i
            Found=True
            break
            
ValidChar=False
while not ValidChar:
    Char=input("Enter a charater among(W, A, S, D) to move.")
    if Char=="W": 
        Characters[Position].ChangePosition(0,1)
        ValidChar=True
    elif Char=="A": 
        Characters[Position].ChangePosition(-1,0)
        ValidChar=True
    elif Char=="S": 
        Characters[Position].ChangePosition(0,-1)
        ValidChar=True
    elif Char=="D": 
        Characters[Position].ChangePosition(1,0)
        ValidChar=True
        
        
print(f"{Characters[Position].GetName()} has changed coordinates to X = {Characters[Position].GetXCoordinate()} and Y = {Characters[Position].GetYCoordinate()}")