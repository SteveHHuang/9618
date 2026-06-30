import datetime

class Character:
    def __init__(self,cn,dob,intelligence,speed):
        self.__CharacterName=cn # PRIVATE CharacterName: STRING
        self.__DateOfBirth=dob # PRIVATE DateOfBirth: DATE
        self.__Intelligence=intelligence # PRIVATE Intelligence: REAL
        self.__Speed=speed # PRIVATE Speed: INTEGER
        
    def GetIntelligence(self): return self.__Intelligence
    def GetName(self): return self.__CharacterName
    
    def SetIntelligence(self,num): self.__Intelligence+=num
    
    def Learn(self): self.__Intelligence+=(self.__Intelligence*0.1)
    
    def ReturnAge(self):
        Year=int(datetime.date.isoformat(self.__DateOfBirth)[0:4])
        return 2023-Year
    
class MagicCharacter(Character):
    def __init__(self, cn, dob, intelligence, speed, ele):
        super().__init__(cn, dob, intelligence, speed)
        # PRIVATE CharacterName: STRING
        # PRIVATE DateOfBirth: DATE
        # PRIVATE Intelligence: REAL
        # PRIVATE Speed: INTEGER
        self.__Element=ele # PRIVATE Element: STRING
    
    def Learn(self):
        if self.__Element=="fire" or self.__Element=="water":
            self.SetIntelligence(self.GetIntelligence()*0.2)
        elif self.__Element=="earth":
            self.SetIntelligence(self.GetIntelligence()*0.3)
        else:
            self.SetIntelligence(self.GetIntelligence()*0.1)
#main
FirstCharacter=Character("Royal", datetime.date(2019,1,1),70,30)
FirstCharacter.Learn()

print(f"Name: {FirstCharacter.GetName()}, Age: {FirstCharacter.ReturnAge()}, Intelligence: {FirstCharacter.GetIntelligence()}")
        
FirstMagic=MagicCharacter("Light", datetime.date(2018,3,3), 75, 22, "fire")
FirstMagic.Learn()

print(f"Name: {FirstMagic.GetName()}, Age: {FirstMagic.ReturnAge()}, Intelligence: {FirstMagic.GetIntelligence()}")
