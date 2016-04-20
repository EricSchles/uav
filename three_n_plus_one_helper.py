import sys
import time

def cycle_length(n):
    count = 1
    while n != 1:
        if n%2!=0:
            n = 3*n+1
        else:
            n /= 2
        count += 1
    return count

dicter = {}
for i in range(10000,1000000):
    dicter[i] = cycle_length(i)

print dicter
