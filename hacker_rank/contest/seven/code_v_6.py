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
    for num_elements in xrange(end-start):        
        if (end-start)+1 >= num_elements:
            summation += sum(generate_sum(num_elements,start,end))
    return summation

def maximum(arr):
    if arr == []:
        return 0
    else:
        return max(arr)

def generate_sum(num_elements,start,end):
    results = []
    for ind,elem in enumerate(a[start:end]):
        if all([ind+i < end for i in xrange(1,num_elements-1)]):
            if ind+num_elements <= end:
                results.append( maximum([a[ind+i] for i in xrange(num_elements)]) )
    return results

        
n,m = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
queries = []
for _ in xrange(m):
    queries.append(map(int,raw_input().strip().split(' ')))

#for query in queries:
#    print F(a,query[0],query[1])
#print F(a,1,3)
print F(a,1,2)
#print F(a,2,3)
