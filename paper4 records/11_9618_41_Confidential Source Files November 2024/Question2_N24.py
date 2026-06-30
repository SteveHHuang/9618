class Horse:
    def __init__(self,n,mfh,ps):
        self.__Name=n # PRIVATE Name: STRING
        self.__MaxFenceHeight=mfh # PRIVATE MaxFenceHeight: INTEGER
        self.__PercentageSuccess=ps # PRIVATE PercentageSuccess: INTEGER
        
    def GetName(self):
        return self.__Name
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self,h,r):
        Probability=self.GetMaxFenceHeight()*0.2
        if h<=self.GetMaxFenceHeight():
            if r==1: Probability=self.__PercentageSuccess*1.0
            elif r==2: Probability=self.__PercentageSuccess*0.9
            elif r==3: Probability=self.__PercentageSuccess*0.8
            elif r==4: Probability=self.__PercentageSuccess*0.7
            elif r==5: Probability=self.__PercentageSuccess*0.6
        return Probability
                
    
class Fence:
    def __init__(self,h,r):
        self.__Height=h # PRIVATE Height: INTEGER
        self.__Risk=r # PRIVATE Risk: INTEGER
        
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk


    
#main
Horses=[] # DECLARE Horses: ARRAY[0:1] OF Horse
Horses.append(Horse("Beauty",150,72))
Horses.append(Horse("Jet", 160, 65))
for horse in Horses:
    print(horse.GetName())
print("")
Course=[] # DECLARE Course: ARRAY[0:3] OF Fence    
for i in range(4):
    Valid=False
    while not Valid:
        h=int(input("Enter the height of the fence in cm (Must between 70 and 180 inclusive). "))
        r=int(input("Enter the risk number of the fence (Must between 1 and 5 inclusive). "))
        if h>=70 and h<=180 and r>=1 and r<=5:
            Valid=True
            Course.append(Fence(h,r))
        else:
            print("Invalid height or risk number.")
Avgs=[]            
for j in range(2):
    sum=0
    for k in range(4):
        print(f"The horse {Horses[j].GetName()} at Fence {k+1} has a {Horses[j].Success(Course[k].GetHeight(),Course[k].GetRisk())}% chance of success")
        sum+=Horses[j].Success(Course[k].GetHeight(),Course[k].GetRisk())
    Avgs.append(sum/4)
    print(f"The horse {Horses[j].GetName()} has an average {Avgs[j]}% chance of jumping all four fences")
if Avgs[0]>Avgs[1]:
    print(f"The horse {Horses[0].GetName()} has the highest average chance of success")
else: print(f"The horse {Horses[1].GetName()} has the highest average chance of success")

