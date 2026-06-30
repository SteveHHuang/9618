def Initialise():
    global Jobs
    global NumberOfJobs
    for x in range(100):
        Jobs[x][0]=-1
        Jobs[x][1]=-1
    NumberOfJobs=0


def AddJob(JobNo,Priority):
    global Jobs
    global NumberOfJobs
    if NumberOfJobs>=100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0]=JobNo
        Jobs[NumberOfJobs][1]=Priority
        NumberOfJobs+=1
        print("Added")
        
def InsertionSort():
    global Jobs
    for i in range(1,NumberOfJobs):
        Job=Jobs[i][0]
        Num=Jobs[i][1]
        HolePosition=i
        UnSorted=True
        while UnSorted and HolePosition>=1:
            UnSorted=False
            if Jobs[HolePosition-1][1]>Num:
                Jobs[HolePosition][0],Jobs[HolePosition][1]=Jobs[HolePosition-1][0],Jobs[HolePosition-1][1]
                HolePosition-=1
                UnSorted=True
        Jobs[HolePosition][0],Jobs[HolePosition][1]=Job,Num
                
def PrintArray():
    global Jobs
    global NumberOfJobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")

#main
Jobs=[[-2 for _ in range(2)]for _ in range(100)]
NumberOfJobs=-2
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)
InsertionSort()
PrintArray()