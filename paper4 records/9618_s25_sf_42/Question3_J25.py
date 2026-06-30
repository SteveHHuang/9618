class Animal:
    def __init__(self,n,sound,size,intelligence):
        self.__Name=n # PRIVATE Name: STRING
        self.__Sound=sound # PRIVATE Sound: STRING
        self.__Size=size # PRIVATE Size: INTEGER
        self.__Intelligence=intelligence # PRIVATE Intelligence: INTEGER
        
    def Description(self):
        return f"The animal's name is {self.__Name}, it makes a {self.__Sound}, its size is {self.__Size} and its intelligence level is {self.__Intelligence}"

class Parrot(Animal):
    def __init__(self,n,sound,size,intelligence,w,nw):
        super().__init__(n, sound, size, intelligence)
        self.__WingSpan=w # PRIVATE WingSpan: INTEGER
        self.__NumberWords=nw # PRIVATE NumberWords: INTEGER
    
    def ChangeNumberWords(self, NewNum):
        self.__NumberWords+=NewNum
    
    def Description(self):
        return (super().Description()+f". It has a wingspan of {self.__WingSpan} cm and can say {self.__NumberWords} words.")

class Wolf(Animal):
    def __init__(self, n, sound, size, intelligence,ts):
        super().__init__(n, sound, size, intelligence)
        self.__TerritorySize=ts # PRIVATE TerritorySize: INTEGER
    
    def SetTerritorySize(self,NewSize):
        self.__TerritorySize+=NewSize
    
    def Description(self):
        return super().Description()+f". Its territory is {self.__TerritorySize} square miles."

#main
Parrot1=Parrot("Chewie","Squawk",1,10,30,29)
Wolf1=Wolf("NightEyes","Howl",8,7,100)
Animal1=Animal("Copper","Neigh",10,6)

Wolf1.SetTerritorySize(-20)
Parrot1.ChangeNumberWords(2)
print(Parrot1.Description())
print(Wolf1.Description())
print(Animal1.Description())
