# 20250618 binarysearch

arr = []

for i in range(100):
    arr.append(i+1)

def binarysearch(num):
    global arr
    lower = 0
    upper = len(arr)-1
    
    while lower <= upper:
        mid = int((lower+upper)/2)
        print(lower,upper, mid)
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            upper = mid - 1
        elif arr[mid] < num:
            lower = mid + 1    
    return False


if __name__ == "__main__":
    print(binarysearch(2))
    
            