import sys

n = input().strip()
arr = [int(elem) for elem in input().strip().split(" ")]

def is_sorted(arr):
    for ind,val in enumerate(arr):
        if ind == len(arr)-1:
            break
        if val > arr[ind+1]:
            return False
    return True

def insertionSort(alist):
    for ind,i in enumerate(arr):
        if ind == len(arr)-1:
            break
        if i > arr[ind+1]:
            position = ind+1
            currentvalue = alist[ind+1]
            break
    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1
        print(" ".join([str(elem) for elem in alist]))
    alist[position]=currentvalue
    return alist
print(" ".join(insertionSort([str(elem) for elem in arr])))

            
