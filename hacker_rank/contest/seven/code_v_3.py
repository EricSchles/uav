def F(a,start,end):
    singleton_only = False
    if start == end:
        singleton_only = True
    summation = 0
    #singletons
    #end -= 1
    start -= 1
    summation += sum([elem for elem in a[start:end]])
    if singleton_only:
        return summation
    #for loop for the rest
    #pairs
    end -= 1
    if (end-start)+1 >= 2:
        summation += sum([max([elem,a[ind+1]]) for ind,elem in enumerate(a[start:end]) if ind+1 <= end])
    #triplets
    if (end-start)+1 >= 3:
        summation += sum([max([elem,a[ind+1],a[ind+2]]) for ind,elem in enumerate(a[start:end]) if ind+1 < end and ind+2 <= end])
    return summation
    
n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(m):
    queries.append(map(int,raw_input().strip().split(' ')))

#for query in queries:
#    print F(a,query[0],query[1])
print F(a,1,3)
#print F(a,1,2)
#print F(a,2,3)
