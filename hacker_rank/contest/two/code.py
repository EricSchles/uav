# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = map(int,raw_input().strip().split(' '))
seq = map(int,raw_input().strip().split(' '))
num_triplets = 0

differencing = {}
for ind,val in enumerate(seq):
    tmp_seq = seq[:ind]+seq[ind+1:]
    for other_val in tmp_seq:
        if other_val < val:
            differencing[str(val)+"_"+str(other_val)] = val - other_val

list_of_candidates = []
for key in differencing:
    if differencing[key] == d:
        print map(int,key.split("_"))
        list_of_candidates.append(map(int,key.split("_")))


for val in list_of_candidates:
    for ind in xrange(len(list_of_candidates)):
        if val[1] == list_of_candidates[ind][0]:
            num_triplets += 1
    
print num_triplets
