n,k = map(int,raw_input().strip().split(' '))
seq = map(int,raw_input().strip().split(' '))

count = 0
seen_pairs = []
for ind,val in enumerate(seq):
    tmp_seq = seq[:ind]+seq[ind+1:]
    for other_val in tmp_seq:
        if val > other_val: 
            if str(val)+"_"+str(other_val) in seen_pairs: continue
        if other_val > val:
            if str(other_val)+"_"+str(val) in seen_pairs: continue
        if abs(other_val - val) == k:
            if val > other_val: seen_pairs.append(str(val)+"_"+str(other_val))
            else: seen_pairs.append(str(other_val)+"_"+str(val))
            count += 1
print(count)
