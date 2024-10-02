import math


primeslist=list()
limit = 10000

def is_prime(x): 
    for n in range (2, math.floor(math.sqrt(x))+1): 
        if x%n == 0:
            return False
    return True

def compats(a, b):
    if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))): return True
    else: return False

def is_compatible(*size):
    if len(size)==2: 
        if compats(size[0], size[1]):
            return True
    if len(size)==3: 
        for term in [size[1],size[2]]:
            if compats(term, size[0]): return True
    if len(size)==4: 


def get_primes(limit):
    global primeslist
    sieve = [True]*limit
    sieve[0]=sieve[1]=[False]
    for n in range(2, limit):
        if sieve[n]==True:
            primeslist.append(n)
            for mult in range(n*2, limit, n):
                sieve[mult]=[False]
                
def generate_families(primes):
    for p in primes: 
        for p2 in primes:
            if p2 == p: continue
            if is_prime(int(str(p)+str(p2))) and is_prime(int(str(p2)+str(p))): 
                for p3 in primes: 
                    if p3==p or p3==p2: continue
                    if 
    




    
get_primes(limit)
print(primeslist)