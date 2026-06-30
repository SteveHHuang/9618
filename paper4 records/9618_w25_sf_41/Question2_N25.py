class Train:
    def __init__(self,id,r):
        self.__TrainIDNumber=id #PRIVATE TrainIDNumber: STRING
        self.__Route=r #PRIVATE Route: INTEGER
        
    def GetTrainIDNumber(self): return self.__TrainIDNumber
    def GetRoute(self): return self.__Route
 
class Station:
    def __init__(self,sid,np):
        self.__StationID=sid #PRIVATE StationID: STRING
        self.__NumberPlatforms=np #PRIVATE NumberPlatforms: INTEGER
        self.__Trains=[] #PRIVATE Trains: ARRAY[0:9] OF Train
        self.__NumberTrains=0 #PRIVATE NumberTrains: INTEGER
    
    def AddTrain(self,Tr):
        if self.__NumberPlatforms<self.__NumberTrains+1:
            return False
        self.__NumberTrains+=1
        self.__Trains.append(Tr)
        
        return True
    
    def GetTrains(self):
        if self.__NumberTrains==0:
            return "There are no trains"
        temp="The trains at station "+self.__StationID+" are:\n"
        for i in range(self.__NumberTrains):
            temp+=(self.__Trains[i].GetTrainIDNumber()+" on the route number "+str(self.__Trains[i].GetRoute())+'\n')
            
        return temp
        
    
#main
Tr1=Train("12ADV",134)
Tr2=Train("33ART",20)
Tr3=Train("9FKF",3)
Tr4=Train("21VBC",24)

St1=Station("STH",2)
St2=Station("NTH",1)

if not St1.AddTrain(Tr1): print("Station is full")
if not St1.AddTrain(Tr2): print("Station is full")
if not St1.AddTrain(Tr3): print("Station is full")
if not St2.AddTrain(Tr4): print("Station is full")

print(St1.GetTrains())
print(St2.GetTrains())
