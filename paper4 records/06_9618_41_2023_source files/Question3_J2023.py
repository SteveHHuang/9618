def PushAnimal(DataToPush):
    global Animal
    global AnimalTopPointer
    
    if AnimalTopPointer==20: 
        return False
    else: 
        Animal[AnimalTopPointer]=DataToPush
        AnimalTopPointer+=1
        return True
    
def PopAnimal():
    global Animal
    global AnimalTopPointer
    
    if AnimalTopPointer==0:
        return ""
    else:
        ReturnData=Animal[AnimalTopPointer-1]
        AnimalTopPointer-=1
        return ReturnData
    
def ReadData():
    try:
        fr=open("AnimalData.txt",'r')
        x=fr.readline().strip()
        while x!="":
            PushAnimal(x)
            x=fr.readline().strip()
        fr.close()
        
        fr1=open("ColourData.txt",'r')
        y=fr1.readline().strip()
        while y!="":
            PushColour(y)
            y=fr1.readline().strip()
        fr1.close()        
    except IOError:
        print("File not found")
        
def PushColour(DataToPush):
    global Colour
    global ColourTopPointer
    
    if ColourTopPointer==10: 
        return False
    else: 
        Colour[ColourTopPointer]=DataToPush
        ColourTopPointer+=1
        return True
    
def PopColour():
    global Colour
    global ColourTopPointer
    
    if ColourTopPointer==0:
        return ""
    else:
        ReturnData=Colour[ColourTopPointer-1]
        ColourTopPointer-=1
        return ReturnData

def OutputItem():
    c=PopColour()
    a=PopAnimal()
    if c=="": 
        PushAnimal(a)
        print("No colour")
    elif a=="":
        PushColour(c)
        print("No Animal")
    else: 
        print(f"{c} {a}")

#main
Animal=["" for _ in range(20)]
Colour=["" for _ in range(10)]
AnimalTopPointer=0
ColourTopPointer=0
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()