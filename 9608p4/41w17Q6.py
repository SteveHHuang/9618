import random

class Animal:
    def __init__(self):
        self.__Across=random.randint(0,39)
        self.__Down=random.randint(0,39)
        self.__Score=0
    
    def getAcross(self):
        return self.__Across
    def setAcross(self, coordinate):
        self.__Across=coordinate
        
    def Move(self):
        NewAcross=self.getAcross()+GenerateChangeInCoordinate(self.getAcross())
        NewDown=self.getDown()+GenerateChangeInCoordinate(self.getDown())
        self.setAcross(NewAcross)
        self.setDown(NewDown)

    
    
class desert:
    def __init__(self):
        self.__Grid=[[None for _ in range(40)] for _ in range(40)]    
        self.__StepCounter=0
        self.__AnimalList=[None for _ in range(20)]
        GenerateFood(self)
        for j in range(5):
            self.__AnimalList.append(Animal)
        
        
    def GenerateFood(self):
        pass
    
def GenerateChangeInCoordinate(x):
    if x>0 or x<39:
        return random.randint(-1,1)
        
]
     
    
# Grid=[[None for _ in range(40)] for _ in range(40)]  

# # for i in range(40):
# #     print(Grid[i])