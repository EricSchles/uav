import sys
import time
from cython_3np1 import find_max_collatz

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
    sol = find_max_collatz(start,end)
    if switched:
        start,end = end,start
        switched = False
    print("{} {} {}".format(start,end,sol))

elapsed = (time.time() - start)
print elapsed - start_time
