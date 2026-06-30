class Balloon:
    def __init__(self,c,d):
        self.__Health=100 #PRIVATE Health: INTEGER
        self.__Colour=c #PRIVATE Colour: STRING
        self.__DefenceItem=d #PRIVATE DefenceItem: STRING
    
    def GetDefenceItem(self): return self.__DefenceItem
    def ChangeHealth(self, num): self.__Health+=num
    def CheckHealth(self):
        if self.__Health<=0: return True
        else: return False
        
def Defend(balloon):
    Strength=int(input("Enter the strength of an opponent"))
    balloon.ChangeHealth(-Strength)
    print(balloon.GetDefenceItem())
    
    if balloon.CheckHealth():
        print("No health remaining")    
    else:
        print("It still has health")
    
    return balloon

#main
Balloon1=Balloon(input("Enter the colour of balloon\n"), input("Enter the defence item of balloon\n"))
Defend(Balloon1)