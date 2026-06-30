class Card:
    def __init__(self,n,c):
        self.__Number=n #PRIVATE Number: INTEGER
        self.__Colour=c #PRIVATE Colour: STRING
        
    def GetNumber(self): return self.__Number
    def GetColour(self): return self.__Colour
    
class Hand:
    def __init__(self,c1,c2,c3,c4,c5):
        self.__Cards=[c1,c2,c3,c4,c5,Card(-1, ""),Card(-1, ""),Card(-1, ""),Card(-1, ""),Card(-1, "")] #PRIVATE Cards: ARRAY[0:9] OF Card
        self.__FirstCard=0 #PRIVATE FirstCard: INTEGER
        self.__NumberCards=5 #PRIVATE NumberCards: INTEGER
   
    def GetCard(self,x):return self.__Cards[x]
    
def CalculateValue(PlayerHand):
    TotalScore=0
    for i in range(5):
        TotalScore+=PlayerHand.GetCard(i).GetNumber()
        if PlayerHand.GetCard(i).GetColour()=="red": TotalScore+=5
        elif PlayerHand.GetCard(i).GetColour()=="blue": TotalScore+=10
        elif PlayerHand.GetCard(i).GetColour()=="yellow": TotalScore+=15
    return TotalScore



#main
C1=Card(1, "red")
C2=Card(2, "red")
C3=Card(3, "red")
C4=Card(4, "red")
C5=Card(5, "red")
C6=Card(1, "blue")
C7=Card(2, "blue")
C8=Card(3, "blue")
C9=Card(4, "blue")
C10=Card(5, "blue")
C11=Card(1, "yellow")
C12=Card(2, "yellow")
C13=Card(3, "yellow")
C14=Card(4, "yellow")
C15=Card(5, "yellow")
Player1=Hand(C1,C2,C3,C4,C11)
Player2=Hand(C12,C13,C14,C15,C6)
if CalculateValue(Player1) > CalculateValue(Player2): print("Player1 wins")
elif CalculateValue(Player1) < CalculateValue(Player2): print("Player2 wins")
else: print("The game was draw")