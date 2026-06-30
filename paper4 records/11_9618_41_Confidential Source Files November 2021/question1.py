def Unknown(x,y):
    if x<y:
        print(x+y)
        return(Unknown(x+1,y)*2)
    else:
        if x==y:
            return 1
        else:
            print(x+y)
            return(Unknown(x-1,y)//2)
        
def IterativeUnknown(m,n):
    result=1
    while m!=n:
        print(m+n)
        if m>n:
            m-=1
            result//=2
        else:
            m+=1
            result*=2
    return result
        
a=10
b=15     
print(f"x={a}, y={b}")
print(f"m={a}, n={b}")  
print(Unknown(a,b))
print(f"IterativeUnknown reselt is: {IterativeUnknown(a,b)}")
b=10
print(f"x={a}, y={b}") 
print(f"m={a}, n={b}")
print(Unknown(a,b))
print(f"IterativeUnknown reselt is: {IterativeUnknown(a,b)}")
a=15
print(f"x={a}, y={b}")
print(f"m={a}, n={b}")
print(Unknown(a,b))
print(f"IterativeUnknown reselt is: {IterativeUnknown(a,b)}")
