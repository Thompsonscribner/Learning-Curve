import math

primeslist=list()
limit = 10000

#checks if any entry is a prime number
def is_prime(x): 
    for n in range (2, math.floor(math.sqrt(x))+1): 
        if x%n == 0:
            return False
    return True

#checks if two numbers when concatinated in both directions (a+b) and (b+a) are both prime numbers
def compats(a, b):
    if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))): return True
    else: return False

# checks compatability for each continuing number, for each itteration. 
# notice how you don't have to check each number against eachother in the len(size)>2, 
# only the newest term (size[0]). This "should" work because it only gets to this 
# iteration with 3 or 4 or 5 values if it all ready passed the level before, meaning 
# they should already be compatable. Let's hope that's true.  
def is_compatible(*size):
    if len(size)==2: 
        if compats(size[0], size[1]):
            return True
    if len(size)> 2: 
        for term in size[1:]:
            if not compats(term, size[0]): return False
        return True

# this is the sieve of eratosthenes function, just giving the original list to work with. 
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
            if is_compatible(p2, p): 
                for p3 in primes: 
                    if p3==p or p3==p2: continue
                    if is_compatible(p3, p2, p):
                        for p4 in primes:
                            if p4==p or p4==p2 or p4==p3: continue
                            if is_compatible(p4, p3, p2, p): 
                                for p5 in primes: 
                                    if p5==p or p5==p2 or p5==p3 or p5==p4: continue
                                    if is_compatible(p5, p4, p3, p2, p):
                                        final = (p5 + p4 + p3 + p2 + p)
                                        print(p5, p4, p3, p2, p)
                                        print(final)
                                        quit()


get_primes(limit)
generate_families(primeslist)