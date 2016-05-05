n = int(raw_input().strip())
found = False
for _ in xrange(n):
    a,m = map(int,raw_input().strip().split(' '))
    squares = [i*i for i in xrange(m)]
    for square in squares: 
        if a == square%m:
            print("YES")
            found = True
            break
    if not found: print("NO")
    else: found = False
