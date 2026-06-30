def IterativeVowels(Value):
    Total=0
    LengthString=len(Value)
    for x in range(LengthString):
        FirstCharacter=Value[0:1]
        if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
            Total+=1
        Value=Value[1:len(Value)]
        
    return Total

def RecursiveVowels(Value):
    Total=0
    if len(Value)==0: 
        return Total
    
    FirstCharacter=Value[0:1]
    if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
        Total+=1
        
    return Total+RecursiveVowels(Value[1:len(Value)])

#main
Sum=IterativeVowels("house")
print(Sum)

Sum1=RecursiveVowels("imagine")
print(Sum1)