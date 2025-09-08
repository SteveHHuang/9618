#Time elapse of iterative fibnacci

import time

# start High-precision timing, bubble sort
start = time.perf_counter()  
def fibnacci(n):
    x1 = 1
    x2 = 1
    if n == 1 or n == 2: return 1
    else:
        for i in range(n-2):
            x1, x2 = x1+x2, x1
        return x1

print(fibnacci(4))
# end timing 
end = time.perf_counter()
print(f"time consumption: {end - start:.6f} second")# Format with 6 decimal places
