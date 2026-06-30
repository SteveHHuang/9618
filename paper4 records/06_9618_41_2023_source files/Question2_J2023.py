class Vehicle:
    def __init__(self,id,ms,ia):
        self.__ID=id # PRIVATE ID: STRING
        self.__MaxSpeed=ms # PRIVATE MaxSpeed: INTEGER
        self.__IncreaseAmount=ia # PRIVATE IncreaseAmount: INTEGER
        self.__CurrentSpeed=0 # PRIVATE CurrentSpeed: INTEGER
        self.__HorizontalPosition=0 # PRIVATE HorizontalPosition: INTEGER
        
    
    def GetCurrentSpeed(self): return self.__CurrentSpeed
    def GetIncreaseAmount(self): return self.__IncreaseAmount
    def GetMaxSpeed(self): return self.__MaxSpeed
    def GetHorizontalPosition(self): return self.__HorizontalPosition
    
    def SetCurrentSpeed(self,s): self.__CurrentSpeed+=s
    def SetHorizontalPosition(self,x): self.__HorizontalPosition+=x
    
    def IncreaseSpeed(self):
        if self.GetCurrentSpeed()+self.GetIncreaseAmount()<=self.GetMaxSpeed():
            self.SetCurrentSpeed(self.GetIncreaseAmount())
            self.SetHorizontalPosition(self.GetCurrentSpeed())
            
class Helicopter(Vehicle):
    def __init__(self, id, ms, ia, vc, mh):
        super().__init__(id, ms, ia)
        self.__VerticalPosition=0 #PRIVATE VerticalPosition: INTEGER
        self.__VerticalChange=vc #PRIVATE VerticalChange: INTEGER
        self.__MaxHeight=mh #PRIVATE MaxHeight: INTEGER
    
    def GetCurrentSpeed(self): return super().GetCurrentSpeed()
    def GetIncreaseAmount(self): return super().GetIncreaseAmount()
    def GetMaxSpeed(self): return super().GetMaxSpeed()
    def GetHorizontalPosition(self): return super().GetHorizontalPosition()
    def GetVerticalPosition(self): return self.__VerticalPosition
    
    def SetCurrentSpeed(self, s): return super().SetCurrentSpeed(s)
    def SetHorizontalPosition(self, x): return super().SetHorizontalPosition(x)
    
    
    def IncreaseSpeed(self):
        if self.__MaxHeight>=self.__VerticalPosition+self.__VerticalChange:
            self.__VerticalPosition+=self.__VerticalChange
        super().IncreaseSpeed()
            
def OutputVehicle(v):
    if type(v)==Vehicle:
        print(f"Horizontal Position: {v.GetHorizontalPosition()}, Current Speed: {v.GetCurrentSpeed()}")
    elif type(v)==Helicopter:
        print(f"Horizontal Position: {v.GetHorizontalPosition()}, Vertical Position: {v.GetVerticalPosition()}, Current Speed:{v.GetCurrentSpeed()}")
        
#main
C1=Vehicle("Tigher",100,20)
C2=Helicopter("Lion",350,40,3,100)

C1.IncreaseSpeed()
C1.IncreaseSpeed()
OutputVehicle(C1)

C2.IncreaseSpeed()
C2.IncreaseSpeed()
OutputVehicle(C2)