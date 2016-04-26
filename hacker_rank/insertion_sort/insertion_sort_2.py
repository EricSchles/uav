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
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1        
        alist[position]=currentvalue
        print(" ".join([str(elem) for elem in alist]))
    return alist
insertionSort(arr)

            
