import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
num_jumps = 0
ind = 0
while ind < len(c)-1:
    print ind,c[ind]
    if ind+2 < len(c):
        if c[ind+1] == 0 and c[ind+2] == 0:
            ind += 2
            num_jumps += 1
        elif c[ind+1] == 0 and c[ind+2] == 1:
            ind += 1
            num_jumps += 1
        elif c[ind+1] == 1 and c[ind+2] == 0:
            ind += 2
            num_jumps += 1
    else:
        ind += 1
        num_jumps += 1
        
print num_jumps
