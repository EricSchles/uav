def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, helper_one, target, helper_two,helper_three)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

def update_rods(dicter):
    rod_one = []
    rod_two = []
    rod_three = []
    rod_four = []
    for disc in dicter.keys():
        if dicter[disc] == 1:
            rod_one.append(disc)
        elif dicter[disc] == 2:
            rod_two.append(disc)
        elif dicter[disc] == 3:
            rod_three.append(disc)
        else:
            rod_four.append(disc)
    return rod_one,rod_two,rod_three,rod_four

N = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
dicter= {}
for ind,val in enumerate(a):
    dicter[ind+1] = val

target, helper_one,helper_two,helper_three = update_rods(dicter)
hanoi(len(a),helper_one,helper_two,helper_three,target)

print source, helper, target
