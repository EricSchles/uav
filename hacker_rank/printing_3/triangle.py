# summation = 0
# for i in range(1,input()):
#     summation += 10**(i-1)
#     print i*summation
#     print i*sum(map(lambda x:10**i-1,range(1,i)))

for i in xrange(1,6):
    print i*sum(map(lambda x: 10**(x-1),range(1,i+1)))

