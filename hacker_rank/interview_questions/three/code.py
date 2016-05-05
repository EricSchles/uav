from itertools import combinations

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

if __name__ == '__main__':
    n,m = map(int,raw_input().strip().split(' '))
    knowledge = []
    for _ in range(n):
        knowledge.append(str(raw_input()).strip())

    combined_knowledges = []
    for combination in combinations(knowledge,2):
        combined_knowledge = ""
        for ind in range(len(combination[0])):
            combined_knowledge += OR(combination[0][ind],combination[1][ind])
        combined_knowledges.append(combined_knowledge)

    maximum = 0
    for combined_knowledge in combined_knowledges:
        num = counter(combined_knowledge)
        if num > maximum:
            maximum = num

    count_of_best = 0
    for combined_knowledge in combined_knowledges:
        if counter(combined_knowledge) == maximum:
            count_of_best += 1

    print(maximum)
    print(count_of_best)
