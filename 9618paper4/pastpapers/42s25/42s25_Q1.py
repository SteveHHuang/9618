#20250923

# a
TopOfStack = -1 # TopOfStack, a global variable of type integer, initialised to -1

Stack = ["-1" for i in range(20)] # Stack, a global 1D array, type of string, all elements are initialised to "-1"

#b
def Push(name):
    global Stack, TopOfStack
    if TopOfStack >= len(Stack)-1:
        return -1
    
    TopOfStack +=1
    Stack[TopOfStack] = name
    
    return 1

#c
def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        return "-1"
    
    
    data = Stack[TopOfStack]
    TopOfStack -=1
    
    return data

#d
def ReadData(FileName):
    global Stack, TopOfStack
    try:
        f = open(FileName, "r")
        for i in range(len(Stack)):
            temp = f.readline()
            temp = temp.strip()
            if temp == '':
                break
            
            result = Push(temp)
    
            if result == -1:
                status = "Stack full"
                print(status)
        
        f.close() 
    except: 
        print("error")

#e        
def Calculate():
    global Stack, TopOfStack
    result = int(Pop())
    status = "okay"
    while status != "-1":
        temp = Pop() 
                
        if temp == "+":
            result += int(Pop())
        elif temp == "-":
            result -= int(Pop())
        elif temp == "/":
            result /= int(Pop())
        elif temp == "*":
            result *= int(Pop())
        elif temp == "^":
            result **= int(Pop())
            
        if temp == "-1":
            status = temp
        
    print(result)
    

#f    
ReadData(input("Enter the name of the file\n"))
Calculate()