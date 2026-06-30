def Enqueue(Num):
    global Queue
    global HeadPointer,TailPointer
    if TailPointer>=100:
        return False
    Queue[TailPointer]=Num
    TailPointer+=1
    if HeadPointer== -1:
        HeadPointer=0
    return True

def RecursiveOutput(Start):
    global Queue
    global HeadPointer,TailPointer
    if Start==TailPointer: return 0
    else: return Queue[Start]+RecursiveOutput(Start+1)

#main
Queue=[-1 for _ in range(100)]
HeadPointer=-1
TailPointer=0

for i in range(1,21):
    if Enqueue(i): print("Successful")
    else: print("Unsuccessful")

print(RecursiveOutput(HeadPointer))