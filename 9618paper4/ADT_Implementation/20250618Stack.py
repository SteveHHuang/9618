# Stack: LIFO, Last in, first out

# 9618 s22 42 Q1
StackData = [0 for i in range(10)] 
# an 1D array with 10 elements, type integer

StackPointer = 0 
# StackPointer points to the next available space in the stack. 
# It is initialised to 0. 
  

def outputElements(): #1b
    global StackData,StackPointer
    for data in StackData:
        print(data)
    print(f"The value of StackPointer is {StackPointer}")
# outputElements() 

def Push(num): #1c
    global StackPointer, StackData
    if StackPointer > 9:
        return False
    
    StackData[StackPointer] = num
    StackPointer += 1
    return True


for i in range(11): #1d
    val = int(input("Please input a number to add "))
    if Push(val):
        print("Successfully added")
    else:
        print("Failed to add")

outputElements()     

def Pop():
    global StackPointer, StackData
    if StackPointer < 0:
        return -1
    StackData[StackPointer-1] = 0
    StackPointer -= 1
    return StackData[StackPointer-1]

for i in range(2):
    Pop()
    
    
print(StackData)
    