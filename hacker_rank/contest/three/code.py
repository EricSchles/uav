#!/bin/python

import sys

def update_dicter(rod_one,rod_two,rod_three,rod_four):
    dicter = {}
    for elem in rod_one:
        dicter[elem] = 1
    for elem in rod_two:
        dicter[elem] = 2
    for elem in rod_three:
        dicter[elem] = 3
    for elem in rod_four:
        dicter[elem] = 4
    return dicter
    
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

def find_next_to_move(rod_one,size):
    biggest = size
    count = 0
    for i in xrange(len(rod_one)):
        if biggest in rod_one:
            biggest -= 1
            count += 1
        if count != i:
            return biggest
    return -1

def get_next_biggest(arr):
    max_elem = max(arr)
    to_remove = arr.index(max_elem)
    tmp = []
    for i in arr[:to_remove]+arr[to_remove+1:]:
        tmp.append(i)
    return max(tmp)

def move_intermediate(next_to_move,rods,index_of_next_to_move):
    for ind,rod in rods:
        if rod == []: return ind
        if max(rod) < next_to_move and ind > index_of_next_to_move:
            return ind
    for ind,rod in rods:
        if max(rod) < next_to_move:
            return ind
    return -1

def move_smaller(elem,rods):
    for ind,rod in enumerate(rods):
        if rod == []: return ind
        if min(rod) > elem:
            return ind
    return -1


N = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
dicter= {}
for ind,val in enumerate(a):
    dicter[ind+1] = val

rod_one,rod_two,rod_three,rod_four = update_rods(dicter)

num_moves = 0
rods = [rod_one,rod_two,rod_three,rod_four]
while find_next_to_move(rods[0],len(a)) != -1:
    next_to_move = find_next_to_move(rods[0],len(a))
    for ind,rod in enumerate(rods):
        if next_to_move in rod:
            index_of_next_to_move = ind

    if max(rods[index_of_next_to_move]) == next_to_move and len(rods[index_of_next_to_move]) != 1:
        while len(rods[index_of_next_to_move]) > 1:
            next_to_move = get_next_biggest(rods[index_of_next_to_move])
            if move_intermediate(next_to_move,rods,index_of_next_to_move) != -1:
                rods[move_intermediate(next_to_move,rods,index_of_next_to_move)].append(next_to_move)
                rods[index_of_next_to_move].remove(next_to_move)
                num_moves += 1
                print rods
                break

    next_to_move = find_next_to_move(rods[0],len(a))
    while any([elem<next_to_move for elem in rods[0]]):
        elements = [elem for elem in rods[0] if elem < next_to_move]
        for elem in elements:
            if move_smaller(elem,rods) != -1:
                rod_ind = move_smaller(elem,rods)
                rods[rod_ind].append(elem)
                rods[0].remove(elem)
                num_moves += 1
                print rods
                break
            
    rods[0].append(next_to_move)
    rods[index_of_next_to_move].remove(next_to_move)
    num_moves += 1
    dicter = update_dicter(*rods)
    print rods
    print num_moves
    if num_moves > 5: break
