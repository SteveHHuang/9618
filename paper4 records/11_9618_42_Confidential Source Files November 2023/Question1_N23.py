def PushData(Letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop
    
    if Letter.lower()=='a' or Letter.lower()=='e' or Letter.lower()=='i' or Letter.lower()=='o' or Letter.lower()=='u':
        if VowelTop >= len(StackVowel):
            print("Stack of vowel full.")
        else:
            StackVowel[VowelTop]=Letter
            VowelTop+=1
    else:
        if ConsonantTop >= len(StackConsonant):
            print("Stack of consonant full.")
        else:
            StackConsonant[ConsonantTop]=Letter
            ConsonantTop+=1

def ReadData():
    try:
        fr=open("StackData.txt",'r')
        
        LetterRead=fr.readline().strip()
        while LetterRead != '':
            PushData(LetterRead)
            LetterRead=fr.readline().strip()
        
        fr.close()
    except IOError:
        print("FILE NOT FOUND.")
        
def PopVowel():
    global StackVowel
    global VowelTop
    
    if VowelTop<=0:
        return "No data"
    
    LetterRead=StackVowel[VowelTop-1]
    VowelTop-=1
    return LetterRead

def PopConsonant():
    global StackConsonant
    global ConsonantTop
    
    if ConsonantTop<=0:
        return "No data"
    
    LetterRead=StackConsonant[ConsonantTop-1]
    ConsonantTop-=1
    return LetterRead

#main
StackVowel=["" for _ in range(100)] # DECLARE StackVowel: ARRAY[0:99] OF STRING
StackConsonant=["" for _ in range(100)] # DECLARE StackConsonant: ARRAY[0:99] OF STRING
VowelTop = 0 # DECLARE VowelTop: INTEGER
ConsonantTop = 0 # DECLARE ConsonantTop: INTEGER

ReadData()
OutputLetters=""
for i in range(5):
    LetterInput=input("Vowel or Consonant? ")
    if LetterInput.lower()=="vowel":
        temp=PopVowel()
        if temp=="No data":
            print("Stack is empty.")
        else:
            OutputLetters+=temp
    elif LetterInput.lower()=="consonant":
        temp=PopConsonant()
        if temp=="No data":
            print("Stack is empty.")
        else:
            OutputLetters+=temp

if temp != "No data": print(OutputLetters)
