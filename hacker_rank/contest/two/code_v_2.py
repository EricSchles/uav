# Enter your code here. Read input from STDIN. Print output to STDOUT
n,d = map(int,raw_input().strip().split(' '))
seq = map(int,raw_input().strip().split(' '))
num_triplets = 0


for ind,elem in enumerate(seq):
    less_pairs = 0
    greater_pairs = 0
    for less_elem in seq[:ind]:
        if elem - less_elem == d:
            less_pairs += 1
    for greater_elem in seq[ind+1:]:
        if greater_elem - elem == d:
            greater_pairs += 1
    num_triplets += min([less_pairs,greater_pairs])
print num_triplets
