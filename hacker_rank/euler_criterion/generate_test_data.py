import random
with open("test_data.txt","w") as f:
    num_cases = random.randint(2000,50000)
    f.write(str(num_cases)+"\n")
    for case in xrange(num_cases):
        f.write(str(random.randint(1,1000))+" "+str(random.randint(1,2000))+"\n")
        
