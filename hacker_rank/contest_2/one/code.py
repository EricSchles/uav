import sys

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

def is_beautiful(string):
    three_grams = ["".join(elem) for elem in find_ngrams(string,3)]
    for gram in three_grams:
        if "010" == gram:
            return False
    return True

def indexes_to_change(string):
    three_grams = ["".join(elem) for elem in find_ngrams(string,3)]
    indices = []
    for ind,gram in enumerate(three_grams):
        if "010" == gram:
            indices.append(ind) 
    return indices

def reorder(B):
    pass

def is_alternating_series(B):
    arr = indexes_to_change(B)
    for ind,val in enumerate(arr):
        if ind == len(arr)-1: break
        if not val+2 == arr[ind+1]:
            return False
    return True

n = int(raw_input().strip())
B = raw_input().strip()

if is_beautiful(B):
    print 0
else:
    count = 0
    for ind,val in enumerate(indexes_to_change(B)):
        alternating = is_alternating_series(B)
        if val >= 2 and ind>1:
            if alternating:
                if val-2 == indexes_to_change(B)[ind-1]:
                    continue
                else:
                    count += 1
        if val>=4 and ind>2:
            if val-2 == indexes_to_change(B)[ind-1] and val-4 == indexes_to_change(B)[ind-2]:
                continue
            else:
                count+=1
        if val>=6 and ind>3:
            if val-2 == indexes_to_change(B)[ind-1] and val-4 == indexes_to_change(B)[ind-2] and val-6 == indexes_to_change(B)[ind-3]:
                continue
            else:
                count += 1
                
        else:
            count += 1
            
print count
