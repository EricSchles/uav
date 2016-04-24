import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positive = [elem for elem in arr if elem >0]
zero = [elem for elem in arr if elem == 0]
negative = [elem for elem in arr if elem < 0]
#print("{0:.2f}".format(a))
print("{0:.6f}".format(len(positive)/float(n)) )
print("{0:.6f}".format(len(negative)/float(n)))
print("{0:.6f}".format(len(zero)/float(n)))
