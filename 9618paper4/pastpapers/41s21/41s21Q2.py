# 9618/41/M/J/21

# 2 a
arrayData = [10,5,6,7,1,12,13,15,21,8]

# 2 bi
def linearSearch(num): 
    global arrayData
    for i in arrayData:
        if i == num:
            return True
    return False


# 2 b ii
try: #test if val is invalid data type
    val = int(input("Enter a number you want to search for:"+"\n"))
    if linearSearch(val) == True:
        print("Search value was found.")
    else:
        print("search value was not found.")    
except: #if val is invalid data type, then output err message
 print("invalid input")


#2 c
def bubbleSort():
    for x in range(10):
        for y in range(9-x):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

# bubbleSort()
# print(arrayData) 