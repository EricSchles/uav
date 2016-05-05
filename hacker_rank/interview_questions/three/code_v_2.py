# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n,m = map(int,raw_input().strip().split(' '))
knowledge = []
for _ in range(n):
    knowledge.append(str(raw_input()).strip())

def OR(a,b):
    if a == "1":
        return "1"
    elif b == "1":
        return "1"
    else:
        return "0"
    
def counter(string):
    count = 0
    for i in string:
        if i == "1":
            count += 1
    return count

combined_knowledges = {}
freq_counts = {}
for combination in combinations(knowledge,2):
    maximum = 0    
    combined_knowledge = "" 
    for ind in range(len(combination[0])):
        combined_knowledge += OR(combination[0][ind],combination[1][ind])

    if combined_knowledge in combined_knowledges.keys():
        freq_counts[combined_knowledge] += 1
    else:
        combined_knowledges[combined_knowledge] = counter(combined_knowledge)
        freq_counts[combined_knowledge] = 1
    if combined_knowledges[combined_knowledge] > maximum: 
        maximum = combined_knowledges[combined_knowledge]
        
print maximum
for key in combined_knowledges.keys():
    if combined_knowledges[key] == maximum: 
        print freq_counts[combined_knowledge]

