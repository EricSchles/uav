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
    while iter < max:
        count = collatz(iter)
        if count > m:
            m = count
            num = iter
        iter += 1
    return num
 
start_time = time.time()
user_input = sys.stdin.read().split("\n")
switched = False
for line in user_input:
    if line == '':
        print()
        continue
        #sys.exit(0)
    start,end = int(line.split(" ")[0]),int(line.split(" ")[1])
    if start > end:
        switched = True
        start,end = end,start
    sol = problem(start,end)
    if switched:
        start,end = end,start
        switched = False
    print("{} {} {}".format(start,end,sol))

elapsed = (time.time() - start)
print "found %s in %s seconds" % (max_found,elapsed)
