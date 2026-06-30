class EventItem:
    def __init__(self,en,t,d):
        self.__EventName=en # PRIVATE EventName: STRING
        self.__Type=t # PRIVATE Type: STRING
        self.__Difficulty=d # PRIVATE Difficulty: INTEGER

    def GetName(self): return self.__EventName
    def GetEventType(self): return self.__Type
    def GetDifficulty(self): return self.__Difficulty

class Character:
    def __init__(self,cn,j,s,r,d):
        self.__CharacterName=cn # PRIVATE CharacterName: STRING
        self.__Jump=j # PRIVATE Jump: INTEGER
        self.__Swim=s # PRIVATE Swim: INTEGER
        self.__Run=r # PRIVATE Run: INTEGER
        self.__Drive=d # PRIVATE Drive: INTEGER

    def GetName(self): return self.__CharacterName

    def CalculateScore(self,Event,Difficulty):
        if Event.lower()=="jump": Difference=Difficulty-self.__Jump
        elif Event.lower()=="swim": Difference=Difficulty-self.__Swim
        elif Event.lower()=="run": Difference=Difficulty-self.__Run
        elif Event.lower()=="drive": Difference=Difficulty-self.__Drive
        
        if Difference<=0: return 100
        elif Difference==1: return 80
        elif Difference==2: return 60
        elif Difference==3: return 40
        elif Difference==4: return 20



#main
Group=[] # DECLARE Group: ARRAY[0:4] OF EventItem
Group.append(EventItem("Bridge","jump",3))
Group.append(EventItem("Water wade","swim",4))
Group.append(EventItem("100 mile run","run",5))
Group.append(EventItem("Gridlock","drive",2))
Group.append(EventItem("Wall on wall","jump",4))

CTarz=Character("Tarz",5,3,5,1)
CGeni=Character("Geni",2,2,3,4)

MarkTarz=0
MarkGeni=0
for i in range(5):
    if CTarz.CalculateScore(Group[i].GetEventType(),Group[i].GetDifficulty())>CGeni.CalculateScore(Group[i].GetEventType(),Group[i].GetDifficulty()):
        print(f"{CTarz.GetName()} wins the event {Group[i].GetName()}")
        MarkTarz+=1
    elif CTarz.CalculateScore(Group[i].GetEventType(),Group[i].GetDifficulty())<CGeni.CalculateScore(Group[i].GetEventType(),Group[i].GetDifficulty()):
        print(f"{CGeni.GetName()} wins the event {Group[i].GetName()}")
        MarkGeni+=1
    else:
        print(f"The event {Group[i].GetName()} is a draw")

if MarkTarz>MarkGeni:
    print(f"{CTarz.GetName()} wins, he has {MarkTarz} points")
elif MarkTarz<MarkGeni:
    print(f"{CGeni.GetName()} wins, he has {MarkGeni} points")
else:
    print("The group is a drew")