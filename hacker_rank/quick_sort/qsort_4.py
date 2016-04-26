def partition(A, lo, hi):
    pivot = A[hi]
    i = lo      # place for swapping
    for j in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j],A[i]
            i += 1
    A[i],A[hi] = A[hi],A[i]    
    return i

def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        print(" ".join([str(elem) for elem in A]))
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)
    

def qsort(alist):
    less = []
    equal = []
    greater = []
    if len(alist) > 1:
        pivot = alist[0]
        for x in alist:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return qsort(less)+equal+qsort(greater)
    else:
        return alist
    
n = int(input().strip())
arr = [int(elem) for elem in input().strip().split(" ")]
quicksort(arr[:],0,n-1)
#print(" ".join([str(elem) for elem in qsort(arr[:])]))
