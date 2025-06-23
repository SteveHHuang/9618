import random 

arr = []

def arrgen():
    global arr
    
    arr = [random.randint(1,1000) for i in range(10)]   