class Character:
    def __init__(self,name,x,y):
        self.__Name=name # PRIVATE Name: STRING
        self.__XPosition=x # PRIVATE XPosition: INTEGER
        self.__YPosition=y # PRIVATE YPosition: INTEGER
    
    def GetXPosition(self): return self.__XPosition
    def GetYPosition(self): return self.__YPosition
    
    def SetXPosition(self,x):
        self.__XPosition+=x
        if self.__XPosition>10000:
            self.__XPosition=10000
        elif self.__XPosition<0:
            self.__XPosition=0
    def SetYPosition(self,y):
        self.__YPosition+=y
        if self.__YPosition>10000:
            self.__YPosition=10000
        elif self.__YPosition<0:
            self.__YPosition=0
            
    def Move(self,Direction):
        if Direction=="up":
            self.SetYPosition(10)
        if Direction=="down":
            self.SetYPosition(-10)
        if Direction=="left":
            self.SetXPosition(-10)
        if Direction=="right":
            self.SetXPosition(10)

class BikeCharacter(Character):
    def __init__(self, Name, XPosition, YPosition):
        super().__init__(Name, XPosition, YPosition)
        # PRIVATE Name: STRING
        # PRIVATE XPosition: INTEGER
        # PRIVATE YPosition: INTEGER
    
    def Move(self, Direction):
        if Direction=="up":
            self.SetYPosition(20)
        if Direction=="down":
            self.SetYPosition(-20)
        if Direction=="left":
            self.SetXPosition(-20)
        if Direction=="right":
            self.SetXPosition(20)
    
#main
Jack=Character("Jack", 50, 50)
Karla=BikeCharacter("Karla", 100, 50)

ValidC1=False
ValidD2=False
while not ValidC1:
    c1=input("Enter the name of the character(Either Jack or Karla) you want to move. ").lower()
    if c1=="jack" or c1=="karla":
        ValidC1=True
    else:
        print("Invalid character name.")
while not ValidD2:        
    d1=input("Enter the direction of the character you want to move(up, down, left or right). ")
    if d1=="up" or d1=="down" or d1=="left" or d1=="right":
        ValidD2=True
    else:
        print("Invalid direction.")
        
if c1=="jack": 
    Jack.Move(d1)
    print(f"Jack's new position is X = {Jack.GetXPosition()} Y = {Jack.GetYPosition()}")
else: 
    Karla.Move(d1)
    print(f"Karla's new position is X = {Karla.GetXPosition()} Y = {Karla.GetYPosition()}")
