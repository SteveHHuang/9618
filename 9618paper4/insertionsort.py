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
     
# ALT version of insertion sort
# modified from 9608/42/M/J/18 Q3b
brr = [4,3,5,7,2]
def InsertionSort(arr):
    for i in range(1, len(arr)):
        HolePosition = i
        temp = arr[i]
        while (HolePosition > 0 and arr[HolePosition-1]>temp):
            arr[HolePosition] = arr[HolePosition-1]
            HolePosition -= 1
            print(arr)
            
        arr[HolePosition] = temp
        print(arr)
        
    
    
InsertionSort(brr)