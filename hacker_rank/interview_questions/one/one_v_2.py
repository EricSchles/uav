n,k = map(int,raw_input().strip().split(' '))
seq = map(int,raw_input().strip().split(' '))

count = 0
seen_pairs = [[],[]]
def dyn_binary_search(elem,array):
    found = []
    firsts = [0]
    lasts = [len(array)-1]
    while firsts[-1] <= lasts[-1]:
        midpoint = (firsts[-1] + lasts[-1])//2
        if elem == array[midpoint]:
            found.append(midpoint)
        elif elem <= array[midpoint]:
            lasts.append(midpoint-1)
        else:
            firsts.append(midpoint+1)
    return found

for ind,val in enumerate(seq):
    tmp_seq = seq[:ind]+seq[ind+1:]
    for other_val in tmp_seq:
        arr_one_found = dyn_binary_search(val,seen_pairs[0])
        arr_two_found = dyn_binary_search(val,seen_pairs[1])
        if arr_one_found != []:
            for found in arr_one_found:
                if seen_pairs[1][found] == other_val: continue
        if arr_two_found != []:
            for found in arr_two_found:
                if seen_pairs[0][found] == other_val: continue
        if abs(other_val - val) == k:
            seen_pairs[0].append(val)
            seen_pairs[1].append(other_val)
            count += 1
print(count)
