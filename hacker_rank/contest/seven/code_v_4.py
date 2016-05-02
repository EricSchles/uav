from itertools import combinations
def maximum(a):
    if a == []:
        return 0
    else:
        return max(a)

def F(a,start,end):
    singleton_only = False
    if start == end:
        singleton_only = True
    summation = 0
    #singletons
    #end -= 1
    start -= 1
    for i in xrange(start,end):
        #for elem in combinations(range(len(a)),i):
            #print maximum([a[j] for j in elem]),i
        summation += sum([maximum([a[j] for j in elem]) for elem in combinations(range(len(a)),i)])
    return summation
    
n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(m):
    queries.append(map(int,raw_input().strip().split(' ')))

for query in queries:
    print F(a,query[0],query[1])
#print F(a,1,3)
