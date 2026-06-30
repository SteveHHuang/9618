#9608 s21 43 Q5b
dataArray=[1,3,5,7,9]

def recursiveBinarySearch(upper,lower,searchvalue):
    global dataArray
    if upper<lower: return -1
    
    mid=(upper+lower)//2
    
    if dataArray[mid] == searchvalue: return mid
    elif dataArray[mid]>searchvalue: return recursiveBinarySearch(mid-1,lower,searchvalue)
    elif dataArray[mid]<searchvalue: return recursiveBinarySearch(upper,mid+1,searchvalue)
    
print(recursiveBinarySearch(4,0,9))