from collections import namedtuple

n = int(raw_input().strip())

def index_of_name(ordering):
    for ind,elem in enumerate(ordering):
        if elem == "NAME":
            return ind
        
ordering = [elem for elem in raw_input().strip().split(" ") if elem != '']
name_index = index_of_name(ordering)
Student = namedtuple("Student",ordering)
students = []
for _ in xrange(n):
    tmp = []
    vals = [elem for elem in raw_input().strip().split(" ") if elem != '']
    for ind,elem in enumerate(vals):
        if ind == name_index:
            tmp.append(str(elem))
        else:
            tmp.append(int(elem))
    students.append(Student(*tmp))

print "{0:.2f}".format(sum([elem.MARKS for elem in students])/float(n))
