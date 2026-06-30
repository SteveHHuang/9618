class Employee:
    def __init__(self,hp,en,jt):
        self.__HourlyPay=hp #PRIVATE HourlyPay: REAL
        self.__EmployeeNumber=en #PRIVATE EmployeeNumber: STRING
        self.__JobTitle=jt #PRIVATE JobTitle: STRING
        self.__PayYear2022=[0.0 for _ in range(52)] #PRIVATE PayYear2022: ARRAY[0:51] OF REAL
        
    def GetEmployeeNumber(self): return self.__EmployeeNumber
    
    def SetPay(self,week,hrs): 
        self.__PayYear2022[week-1]=hrs*self.__HourlyPay
        
    def GetTotalPay(self):
        result=0
        for num in self.__PayYear2022:
            result+=num
        return result
    
class Manager(Employee):
    def __init__(self, hp, en, jt, bv):
        super().__init__(hp, en, jt)
        self.__BounusValue=bv #PRIVATE BounusValue: REAL
        
    def SetPay(self, week, hrs):
        hrs+=(self.__BounusValue/100)*hrs
        super().SetPay(week, hrs)
 
def EnterHours():
    global EmployeeArray
    fr1=open("HoursWeek1.txt",'r')
    x=fr1.readline().strip()
    while x != "":
        id=x
        hrs=float(fr1.readline().strip())
        for staff in EmployeeArray:
            if staff.GetEmployeeNumber() == id:
                staff.SetPay(1,hrs)
                
        x=fr1.readline().strip()
    fr1.close()
    
    
#main
EmployeeArray=[Employee(-0.1,"","") for _ in range(8)]
fr=open("Employees.txt",'r')
x=fr.readline().strip()
count=0
while x != "":
    HourPay=float(x)
    EmNum=fr.readline().strip()
    temp=fr.readline().strip()
    if temp[0]>="A" and temp[0]<="Z":
        jt=temp
        EmployeeArray[count]=Employee(HourPay,EmNum,jt)
    else:
        bv=float(temp)
        jt=fr.readline().strip()
        EmployeeArray[count]=Manager(HourPay,EmNum,jt,bv)
        
    count+=1
    x=fr.readline().strip()
    
fr.close()

EnterHours()
for staff in EmployeeArray:
    print(f"Employee number:{staff.GetEmployeeNumber()}, Total pay:{staff.GetTotalPay()}")