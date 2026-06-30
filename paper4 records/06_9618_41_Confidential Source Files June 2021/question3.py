class TreasureChest:
    def __init__(self,question,answer,pts):
        self.__question=question # Stores the question, data type of string
        self.__answer=answer # Stores the answer, data type of integer
        self.__points=pts # Stores the maximum possible number of points avaliable for this chest, data type of integer
        
    def getQuestion(self):
        return self.__question
    def checkAnswer(self,num):
        if num==self.__answer: return True
        return False
    
    def getPoints(self,NoOfAttempts):
        if NoOfAttempts==1:return self.__points
        elif NoOfAttempts==2: return self.__points // 2
        elif NoOfAttempts==3 or NoOfAttempts==4: return self.__points // 4
        else: return 0
        
def readData():
    global arrayTreasure
    try:
        temparr=[None for _ in range(3)]
        f=open("TreasureChestData.txt",'r')
        for j in range(5):
            for i in range(3):
                temparr[i]=f.readline().strip()
            arrayTreasure.append(TreasureChest(temparr[0],int(temparr[1]),int(temparr[2])))
            
        f.close()
    except:
        print("File not found")
    
    


if __name__ =='__main__':
    arrayTreasure=[]
    readData()
    QNo=int(input("Enter a aquestion number between 1 and 5.\n"))
    print(arrayTreasure[QNo-1].getQuestion())
    Count=1
    while arrayTreasure[QNo-1].checkAnswer(int(input("Enter your answer.\n"))) is False:
        Count+=1
    print(f"You got {arrayTreasure[QNo-1].getPoints(Count)} marks in this question.")