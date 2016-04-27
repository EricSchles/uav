n = int(raw_input())
scores = {}
def avg(scores):
    return sum(scores)/float(len(scores)) 

for i in range(n):
    line = raw_input().split(" ")
    scores[line[0]] = avg([int(elem) for elem in line[1:]])
print "{0:.2f}".format(scores[str(raw_input())])
