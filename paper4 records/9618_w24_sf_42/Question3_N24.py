def ReadData():
    try:
        fr=open("HighScoreTable.txt",'r')

        Array=[]
        x=fr.readline().strip()
        while x != "":
            Id=x
            Level=fr.readline().strip()
            Score=fr.readline().strip()
            x=fr.readline().strip()
            Array.append([Id,Level,Score])

        fr.close()
        return Array
    except IOError:
        print("File not found.")

def OutputHighScores(Array2D):
    for info in Array2D:
        print(f"{info[0]} reached level {info[1]} with a score of {info[2]}")

def SortScores(Array2D):
    Terminal=len(Array2D)-1
    Swapped=True
    while Swapped and Terminal>0:
        Swapped=False
        for i in range(Terminal):
            if (int(Array2D[i][1])<int(Array2D[i+1][1])) or (int(Array2D[i][1])==int(Array2D[i+1][1]) and int(Array2D[i][2])<int(Array2D[i+1][2])):
                Temp1=Array2D[i][0]
                Temp2=Array2D[i][1]
                Temp3=Array2D[i][2]
                Array2D[i][0]=Array2D[i+1][0]
                Array2D[i][1]=Array2D[i+1][1]
                Array2D[i][2]=Array2D[i+1][2]
                Array2D[i+1][0]=Temp1
                Array2D[i+1][1]=Temp2
                Array2D[i+1][2]=Temp3
                Swapped=True
        Terminal-=1
    SortedArray=Array2D
    return SortedArray


#main
HighScores=[["" for j in range(3)] for i in range(7)] #DECLARE HighScores: ARRAY[0:6, 0:3] OF STRING
HighScores=ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores=SortScores(HighScores)
print("After")
OutputHighScores(HighScores)