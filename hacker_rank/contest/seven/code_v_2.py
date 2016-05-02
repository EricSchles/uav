def F(A,start,end):
    start -= 1
    summation = 0
    end_range = range(start,end)
    print "end_range",end_range
    while end_range != []:
        for end in end_range:
            print "Start",start
            print "end",end
            if start == end:
                print "max",A[start]
                summation += A[start]
            else:
                print "max",max(A[start:end+1])
                summation += max(A[start:end+1])
        start += 1
        if start == end:
            end_range = range(start,end+1)
            print "end_range",end_range
        else:
            end_range = range(start,end)
    return summation

n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(m):
    queries.append(map(int,raw_input().strip().split(' ')))

print F(a,1,3)
#for query in queries:
#    print F(a,query[0],query[1])

