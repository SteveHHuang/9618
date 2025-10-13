import random

OpenHashTable = [None for _ in range(2000)]
Divisor = 2000
Stri = ""
def Hashing():
    global OpenHashTable, Divisor, Stri
    x = random.randint(0,10000)

    if OpenHashTable[(x)%Divisor] is None:
        OpenHashTable[(x)%Divisor] = x
        Stri += f"{(x)%Divisor}"
        
    else: 
        i = 1
        OutOfRange = False
        while OpenHashTable[((x) + (i**3))%Divisor] is not None:
            i +=1
            if ((x) + (i**3)%Divisor)>=len(OpenHashTable):
                print("out of range")
                OutOfRange = True
                break
            
        if not OutOfRange:
            OpenHashTable[((x) + (i**3))%Divisor] = x
            Stri += f"{((x) + (i**3))%Divisor}"
        
for i in range(10000):
    Hashing()
    
print(Stri)
print(OpenHashTable)