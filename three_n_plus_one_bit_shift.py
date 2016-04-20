import sys

user_input = sys.stdin.read().split("\n")
switched = False
for line in user_input:
    if line == '':
        print()
        continue
        #sys.exit(0)
    a,b = int(line.split(" ")[0]),int(line.split(" ")[1])
    if a<b: start,end = a,b 
    else: start,end = b,a
    cyclemax = -1
    for n in range(start,end+1):
        cycle=1
        while n!=1:
            if n %2 != 0: n = 3*n+1
            else: n >>=1
            cycle += 1
        if cycle > cyclemax: cyclemax = cycle
    print("{} {} {}".format(start,end,cyclemax))
