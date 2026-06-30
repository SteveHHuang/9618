class Card:
    def __init__(self,Num, CardColour):
        self.__Number=Num # PRIVATE Number: INTEGER
        self.__Colour=CardColour # PRIVATE Colour: STRING
    
    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    
# def ChooseCard():
#     index=int(input("Enter a number between 1 and 30. "))
#     if index>=1 and index <=30:
#         if CardSelection[index-1] is False:
#             CardSelection[index-1]=True
#             return index-1
#         else:
#             while CardSelection[index-1]:
#                 index=int(input("Enter a number between 1 and 30. "))
#                 if index>=1 and index <=30:
#                     if CardSelection[index-1] is False:
#                         CardSelection[index-1]=True
#                         return index-1

def ChooseCard():
    global NumbersChosen
    flagContinue = True
    while flagContinue == True:
        CardSelected = int(input("Select a Card from 1 to 30"))
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30")
        elif NumbersChosen[CardSelected - 1] == True:
            print("Already taken")
        else:
            print("Valid")
            flagContinue = False
            NumbersChosen[CardSelected-1] = True
    return CardSelected-1


# main
ArrayCard=[Card(-1,"") for _ in range(30)] # DECLARE ArrayCard: ARRAY[1:30] OF Card
CardSelection=[False for _ in range(30)] # DECLARE CardSelection: ARRAY[1:30] OF BOOLEAN
file=open("CardValues.txt", 'r')
count=0
for item in file:
    if item != "":
        Num=int(item)
        Colour=file.readline().strip()
        ArrayCard[count]=Card(Num,Colour)
        count+=1
        
Player1=[Card(-1,"") for _ in range(4)] # DECLARE Player1: ARRAY[1:4] OF Card

for j in range(4):
    Player1[j]=ArrayCard[ChooseCard()]
for Cards in Player1:
    print(f"Number: {str(Cards.GetNumber()).strip()}, Colour: {Cards.GetColour()}")
    
