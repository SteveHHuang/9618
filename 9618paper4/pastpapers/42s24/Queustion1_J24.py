WordArray = [None]
NumberWords = None

# def ReadWords(name):
    
#     global WordArray, NumberWords
#     f = open(name, "r")
    
#     count = 0
#     while True:
#         temp = f.readline().strip()
#         print(temp)
#         if temp == '':
#             break
#         count+=1
#         if count == 1:
#             WordArray[0]=f.readline().strip()
#             NumberWords = count-1
#         else: WordArray.append(f.readline().strip())
#     Play()

# filename = input("Enter the name of the file, Enter 'easy', 'medium' or 'hard' ONLY.")
# if filename == "easy":
#     ReadWords("Easy.txt")
# elif filename == "medium":
#     ReadWords("Medium.txt")
# else:
#     ReadWords("Hard.txt")

def Play():
    global WordArray, NumberWords
    print(WordArray[0])
    print()
    count = 0
    response = input("Enter the words?, enter 'no' if you want to exit.")
    while response != "no":
        for i in range(len(WordArray)):
            if WordArray[i] == response:
                print(f"{response} is a correct answer.")
                count +=1
                WordArray[i] = None
            else:
                print(f"{response} is an incorrect answer.")
                response = input("Enter the words, enter 'no' if you want to exit.")
    if response == "no":
        for i in range(1,len(WordArray)):
            print(f"You have found {(count/NumberWords)*100}% of total answers.")
            if WordArray != None:
                print(WordArray[i])
                
def ReadWords(name):
    
    global WordArray, NumberWords
    f = open(name, "r")
    NumberWords = -1
    count = 0
    while True:
        temp = f.readline().strip()
        print(temp)
        if temp == '':
            break
        count+=1
        if count == 1:
            WordArray[0]=temp
            NumberWords +=1
        else: WordArray.append(temp)
    Play()
            
                

filename = input("Enter the name of the file, Enter 'easy', 'medium' or 'hard' ONLY.")
if filename == "easy":
    ReadWords("Easy.txt")
elif filename == "medium":
    ReadWords("Medium.txt")
else:
    ReadWords("Hard.txt")
    