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



def main():
    user_input = sys.stdin.read().split("\n")
    switched = False
    for line in user_input:
        if line == '':
            print()
            sys.exit(0)
        start,end = process_input(line)
        if start > end:
            switched = True
            start,end = end,start 
        cycles = []
        for i in range(start,end+1):
            if i < 10000:
                cycles.append(cycle_length(i))
            else:
                cycles.append(lookup[i])
            if switched:
                start,end = end,start
                switched = False
        print(str(start)+" "+str(end)+" "+str(max(cycles)))

if __name__ == '__main__':
    main()

