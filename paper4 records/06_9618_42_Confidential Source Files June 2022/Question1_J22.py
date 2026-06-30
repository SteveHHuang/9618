def OutputStack():
    global StackPointer
    for item in StackData:
        print(item)
    print(StackPointer)

def Push(num):
    global StackPointer
    if StackPointer == len(StackData):
        return False
    StackData[StackPointer]=num
    StackPointer+=1
    return True

def Pop():
    global StackPointer
    if StackPointer==0: return -1
    
    num=StackData[StackPointer-1]
    StackPointer-=1
    return num

# main
StackData=[-1 for _ in range(10)]
StackPointer=0
for i in range(11):
    if Push(int(input("Input a number to add onto the stack. "))): print("Successfully added.")
    else: print("Stack full.")
OutputStack()
Pop()
Pop()
OutputStack()