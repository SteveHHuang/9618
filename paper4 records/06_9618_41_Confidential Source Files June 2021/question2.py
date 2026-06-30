def linearSearch(Num):
    global arrayData
    for num in arrayData:
        if Num == num:
            return True

    return False

def bubbleSort():
    global arrayData
    for x in range(0,10):
        for y in range(0,10-x-1):
            if arrayData[y]<arrayData[y+1]:
                temp=arrayData[y]
                arrayData[y]=arrayData[y+1]
                arrayData[y+1]=temp



if __name__ =='__main__':
    arrayData=[10,5,6,7,1,12,13,15,21,8]
    # if linearSearch(int(input("Enter an integer number.\n"))): print("The number is in the list.")
    # else: print("The number is not in the list.")
    
    bubbleSort()
    print(arrayData)