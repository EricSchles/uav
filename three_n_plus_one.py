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

def process_input(string):
    start,end = [int(elem) for elem in string.split(" ") if elem != '']
    return start,end

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
    cycles = []
    for i in range(start,end+1):
        cycles.append(cycle_length(i))
    if switched:
        start,end = end,start
        switched = False
    print("{} {} {}".format(start,end,max(cycles)))

time_diff = time.time() - start_time
print("Took"+str(time_diff))
