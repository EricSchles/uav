import sys

V = int(input().strip())
size = input().strip()
arr = [int(elem) for elem in input().strip().split(" ")]

print(arr.index(V))
