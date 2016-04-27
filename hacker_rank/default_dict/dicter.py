# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

d = defaultdict(list)
n,m = [int(elem) for elem in raw_input().split(" ")]
for _ in xrange(n):
    d["A"].append(raw_input().strip())
for _ in xrange(m):
    d["B"].append(raw_input().strip())

indices = []
for word_b in d["B"]:
    tmp = []
    for index,word_a in enumerate(d["A"]):
        if word_b == word_a:
            tmp.append(index+1)
    if tmp == []:
        indices.append([-1])
    else:
        indices.append(tmp)
        
for indexes in indices:
    print " ".join([str(elem) for elem in indexes])
