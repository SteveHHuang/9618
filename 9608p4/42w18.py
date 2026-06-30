class Performer:
    def __init__(self,FName,LName,SRole,SN0,Perf):
        self._FirstName=FName
        self._LastName=LName
        self._SecondRole=SRole
        self._StageName=SN0
        self._PerfType=Perf
        
    def EditSecondaryRole(self,R):
        self._SecondRole=R
        
    def EditStageName(self,SN):
        self._StageName=SN
    
class Acrobat(Performer):
    def __init__(self,FName,LName,SRole,SN0,FireState):
        super().__init__(FName,LName,SRole,SN0,"Acrobat")
        self.__UseFire=FireState
        
    def PerformerInfo(self):
        if self.__UseFire: FireOrNot="is"
        else: FireOrNot="is not"
        
        print(f"{self._StageName} (real name {self._FirstName} {self._LastName}) is an Acrobat. Fire {FireOrNot} part of {self._StageName}'s act. When not performing, {self._StageName} is a {self._SecondRole}")
        
    
Acrobat_1=Acrobat("Alex","Tan","popcorn seller", "Amazing Alex", True)
Acrobat_1.PerformerInfo()