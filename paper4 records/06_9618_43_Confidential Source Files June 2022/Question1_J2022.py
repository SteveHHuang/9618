def ReadHighScores():
    global Name
    global Mark
    fr=open("HighScore.txt",'r')
    for i in range(10):
        Name[i]=fr.readline().strip()
        Mark[i]=int(fr.readline().strip())
    fr.close()

def OutputHighScores():
    global Name
    global Mark
    print("PlayerName | Score")
    for i in range(11):
        print(f"{Name[i]} {Mark[i]}")
def NewtopScores(name, mark):
    global Mark
    global Name
    temp=-1
    for i in range(10):
        if Mark[i]<mark:
            temp=i
            break
    if temp!=-1:
        for k in range(10,temp+1,-1):
            Name[k]=Name[k-1]
            Mark[k]=Mark[k-1]
        Name[temp]=name
        Mark[temp]=mark
    
def WriteTopTen():
    global Mark
    global Name     
    fw=open("NewHighScore.txt",'w')
    for i in range(10):
        fw.write(Name[i]+'\n')
        fw.write(str(Mark[i])+'\n')
    fw.close()

#main
Name=["[NULL]" for _ in range(11)]
Mark=[-1 for _ in range(11)]
ReadHighScores()
OutputHighScores()

Invalid=True
while Invalid:
    name=input("Enter a new player name(3 characters ONLY). ")
    score=int(input("Enter a new player score(Between 1 and 100000 inclusive). "))
    if len(name)==3 and score>=1 and score<=1000000:
        Name[10]=name
        Mark[10]=score
        Invalid=False
    else: print("INVALID name or score")
    
NewtopScores(name,score)
OutputHighScores()
WriteTopTen()