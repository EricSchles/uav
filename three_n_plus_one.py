import sys

def memoized(fn):
    memoized_lengths = [0] * 1000000000
    def fn2(n):
        try:
            memoized_lengths[n]
        except:
            print(n)
        if not memoized_lengths[n]:
            memoized_lengths[n] = fn(n)
        return memoized_lengths[n]
    return fn2

@memoized
def cycle_length(n):
    if n == 1: return 1
    if n % 2:
        return cycle_length(n * 3 + 1) + 1
    return cycle_length(n // 2) + 1
    
def problem(i,j):
    return max([cycle_length(x) for x in range(i, j+1)])

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
