global Stack # DECLARE Stack: ARRAY[0:19] OF STRING
global TopOfStack # DECLARE TopOfStack: INTEGER

def Push(Data):
    global Stack
    global TopOfStack
    
    if TopOfStack+1>=20:
        return -1
    
    TopOfStack+=1
    Stack[TopOfStack]=Data
    return 1

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack<0:
        return "-1"
    TopOfStack-=1
    return Stack[TopOfStack+1]

def ReadData(FileName):
    try:
        f=open(FileName, 'r')
        
        x=f.readline().strip()
        while x!="":
            if Push(x)==-1:
                print("Stack full")
            x=f.readline().strip()
        f.close()
    except IOError:
        print("File not found.")

def Calculate():
    Total=int(Pop())
    x=Pop()
    while x!="-1":
        if x=="+": Total+=int(Pop())
        elif x=="-": Total-=int(Pop())
        elif x=="*": Total*=int(Pop())
        elif x=="/": Total/=int(Pop())
        elif x=="^": Total**=int(Pop())
        x=Pop()
    return Total
            

#main
Stack=["-1" for _ in range(20)]
TopOfStack=-1

FName=input("Enter a filename. ")
ReadData(FName)
print(Calculate())

