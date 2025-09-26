WordArray = [None]
NumberWords = None


def Play():
    global WordArray, NumberWords
    print(WordArray[0])
    
    count = 0
    response = input("Enter the words, enter 'no' if you want to exit.\n")
    while response != "no":
        Found = False
        for i in range(len(WordArray)):
            if WordArray[i] == response:
                temp = i
                Found = True

        if Found:    
            print(f"{response} is a correct answer.")
            count +=1
            WordArray[temp] = None
        else:
            print(f"{response} is an incorrect answer.")
        
        response = input("Enter the words, enter 'no' if you want to exit.\n")
            
    if response == "no":
        print(f"You have found {(count/NumberWords)*100}% of total answers.")
        for i in range(1,len(WordArray)):
            
            if WordArray[i] != None:
                print(WordArray[i])
                
def ReadWords(name):
    
    global WordArray, NumberWords
    f = open(name, "r")
    NumberWords = -1
    count = 0
    while True:
        temp = f.readline().strip()
        
        if temp == '':
            break
        count+=1
        if count == 1:
            WordArray[0]=temp
            
        else: 
            WordArray.append(temp)
        
        NumberWords +=1
    Play()
            
                

filename = input("Enter the name of the file, enter 'easy', 'medium' or 'hard' ONLY.\n")
if filename == "easy":
    ReadWords("Easy.txt")
elif filename == "medium":
    ReadWords("Medium.txt")
else:
    ReadWords("Hard.txt")
    