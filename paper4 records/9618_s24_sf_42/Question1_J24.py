def ReadWords(FileName):
    global WordArray
    global NumberWords
    fr=open(FileName, 'r')
    
    x=fr.readline().strip()
    
    while x!="":
        WordArray.append(x)
        NumberWords+=1
        x=fr.readline().strip()
    NumberWords-=1
    fr.close()
    
    Play()

def Play():
    global WordArray
    global NumberWords

    print(f"Main word: {WordArray[0]}\nNumber of answers: {NumberWords}")
    CorrectAns=0
    Exit=False
    while not Exit:
        InputWord=input("Enter a word, or enter 'no' to exit. ").lower()
        if InputWord=="no":
            Exit=True
            print(f"You entered {(CorrectAns/NumberWords)*100}% of answers.")
            print("Here's the remaining answers.")
            for j in range(1,len(WordArray)):
                if WordArray[j] is not None:
                    print(WordArray[j])
        else:
            Correct=False
            for j in range(1,len(WordArray)):
                if WordArray[j]==InputWord:
                    print(f"Your answer: [{InputWord}] is a CORRECT answer.")
                    Correct=True
                    CorrectAns+=1
                    WordArray[j]=None
                    break
            if not Correct:
                print(f"Your answer: [{InputWord}] is an INCORRECT answer.")
    
#main
WordArray=[]
NumberWords=0

Level=input("Choose one of the difficulty among 'easy', 'medium' and 'hard'. ").lower()
if Level=="easy": ReadWords("Easy.txt")
elif Level=="medium": ReadWords("Medium.txt")
elif Level=="hard": ReadWords("Hard.txt")
