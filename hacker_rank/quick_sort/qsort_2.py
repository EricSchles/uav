import sys

size = int(input().strip())
array = [int(elem) for elem in input().strip().split(" ")]

def qsort(alist):
    less = []
    equal = []
    greater = []
    if len(alist) > 1:
        if len(alist) != size:
            listing = alist[:]
            listing.sort()
            print(" ".join([str(elem) for elem in listing]))
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

print(" ".join([str(elem) for elem in qsort(array)]))
