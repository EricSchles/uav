import sys
import time
 
cdef collatz(unsigned int n):
    cdef unsigned count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count
 
cdef find_max_collatz(unsigned int min, unsigned int max):
    cdef unsigned int m = 1
    cdef unsigned long num = 1
    cdef unsigned int count = 1
    cdef unsigned long iter = min
    while iter < max+1:
        count = collatz(iter)
        if count > m:
            m = count
            num = iter
        iter += 1
    return m
 
