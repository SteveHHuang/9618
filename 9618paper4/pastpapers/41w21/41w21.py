def Unknown(x, y): # x and y are integer parameters
    if x < y:
        print(x+y)
        return (Unknown(x+1,y)*2)
    elif x == y:
            return 1
    else:
        print(x+y)
        return(Unknown(x-1, y)//2)

x = 10
y = 15
print(Unknown(x,y), x, y)
print(Unknown(x,x), x, x)
print(Unknown(y,x), y, x)
   

def IterativeUnknown(x, y): # x and y are integer parameters
    count = 1
    while x != y:
        if x <=y:
            print(x+y)
            x+=1
            count *=2
        else:
            print(x+y)
            x-=1
            count //2
    return count 
            
