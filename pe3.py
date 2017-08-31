import math
pf = 0
num = 600851475143
#num = 13195
for x in range (2,num):
    prime = False
    if(num % x == 0):
        for y in range (2, int(math.sqrt(x))+1):
            
            if(x % y == 0):
                prime = False
                break
                         
            prime = True
        if(prime == True):
            print('prime num: %d' % (x))
            if(x > pf):
                pf = x
                print('highest prime: %d' % (pf))