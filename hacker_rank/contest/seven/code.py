def F(A,start,end):
    #zero indexing
    start -= 1   
    summation = 0
    start_update = 0
    end_update = end
    while start+start_update <= end:
        if end_update == 0:
            start_update += 1
            end_update = end-start_update
        if start == end:
            summation += A[start]
        elif start+start_update == end-end_update:
            summation += A[start+start_update]
        else:
            print "start",start
            print "start+update",start+start_update
            print "end",end
            print "end+update",end-end_update
            print "end_update",end_update
            print A[start+start_update:end-end_update]
            print "summation",summation
            summation += max(A[start+start_update:end-end_update])
        end_update -= 1
    return summation

n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(m):
    queries.append(map(int,raw_input().strip().split(' ')))

for query in queries:
    print F(a,query[0],query[1])
