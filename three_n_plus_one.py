import sys

lookup = {}
user_input = sys.stdin.read().split("\n")
switched = False
for line in user_input:
    if line == '':
        print()
        #continue
        sys.exit(0)
    start,end = int(line.split(" ")[0]),int(line.split(" ")[1])
    if start > end:
        switched = True
        start,end = end,start 
    cycles = []
    for n in range(start,end+1):
        count = 1
        if n in lookup:
            count = lookup[n]
        else:
            while n != 1:
                if n%2!=0:
                    n = 3*n+1
                else:
                    n /= 2
                count += 1
            lookup[n] = count
        cycles.append(count)
    if switched:
        start,end = end,start
        switched = False
    print("{} {} {}".format(start,end,max(cycles)))
