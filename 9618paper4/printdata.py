def printData(numbers):
    line = 0
    for n in numbers:
        print(n, end=" ")
        line +=1
        if line %10 ==0:
            print()