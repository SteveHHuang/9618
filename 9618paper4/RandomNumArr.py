#20250604
import random

count = 0
arr = []

for i in range(1000):
    arr.append(random.randint(1,1000))
    
for num in arr:
    print(num, end=" ")
    count +=1
    if count %10 == 0:
        print()
        
          
# bubble sort        
for j in range(999, 0, -1):
    for k in range (j):
        if arr[k+1] < arr[k]:
            temp = arr[k+1]
            arr[k+1] = arr[k]
            arr[k] = temp
        
print(arr)

