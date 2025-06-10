arr = [5, 2, 4, 6, 1, 3]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        tempnum = arr[i]
        while j >= 0 and arr[j] >= tempnum:
            arr[j+1]=arr[j] 
            j -= 1
        arr[j+1] = tempnum
            

insertion_sort(arr)
print(arr)       
     