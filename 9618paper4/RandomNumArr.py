#20250604
import random

count = 0
arr = []
j = 1000


for i in range(j):
    arr.append(random.randint(1,1000))
    
for num in arr:
    print(num, end=" ")
    count +=1
    if count %10 == 0:
        print()
        
          
# bubble sort        
while True:
    swap = False
    for k in range (j-1):
        if arr[k+1] < arr[k]:
            temp = arr[k+1]
            arr[k+1] = arr[k]
            arr[k] = temp
            swap = True
    j -= 1
    if swap == False:
        break        
    
    
    

print(arr)

