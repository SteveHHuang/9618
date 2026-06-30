def Push(Num):
    global Stack
    global TopOfStack
    if TopOfStack>=len(Stack)-1:
        return False
    Stack[TopOfStack]=Num
    TopOfStack+=1
    return True

def Pop():
    global Stack
    global TopOfStack
    if TopOfStack<0: 
        return -999
    Num=Stack[TopOfStack]
    TopOfStack-=1
    return Num

def FindValues(): 
    Empty=False
    count=0
    while not Empty:
        count+=1
        Num=Pop()  
        if Num==-999:
            print(f"The largest number that was in the stack is {Max}.\nThe smallest number that was in the stack is {Min}.")
            Empty=True
        if count==1:
            Max=Num
            Min=Num
            
        if Num<Min: Min=Num
        elif Num>Max: Max=Num
            


import random

# main
Stack=[-99 for _ in range(30)]
TopOfStack=-1

for i in range(40):
    if not Push(random.randint(0,1000)):
        print("Stack full")
        break
  
FindValues()