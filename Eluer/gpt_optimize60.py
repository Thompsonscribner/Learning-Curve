# This is the code chatgpt generates when I ask
# it to optimize my code. it runs at seconds. 


import math

primeslist = []
limit = 10000
prime_set = set()  # To store primes for quick lookup
compat_cache = {}  # To store compatible pairs

# Optimized is_prime using memoization (checked by prime_set)
def is_prime(x):
    if x in prime_set:  # Fast lookup in prime_set
        return True
    if x < 2:
        return False
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True

# Cache prime compatibility checks
def compats(a, b):
    key = (a, b)
    if key in compat_cache:
        return compat_cache[key]
    
    concat1 = int(str(a) + str(b))
    concat2 = int(str(b) + str(a))
    result = is_prime(concat1) and is_prime(concat2)
    
    compat_cache[key] = result  # Cache the result for this pair
    return result

# Checks compatibility for multiple primes, as optimized above
def is_compatible(*size):
    last = size[0]
    for term in size[1:]:
        if not compats(term, last):
            return False
    return True

# Optimized Sieve of Eratosthenes to generate prime list
def get_primes(limit):
    global primeslist, prime_set
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for n in range(2, limit):
        if sieve[n]:
            primeslist.append(n)
            prime_set.add(n)
            for mult in range(n * 2, limit, n):
                sieve[mult] = False

def generate_families(primes):
    for i, p in enumerate(primes):
        for j in range(i + 1, len(primes)):
            p2 = primes[j]
            if is_compatible(p, p2):
                for k in range(j + 1, len(primes)):
                    p3 = primes[k]
                    if is_compatible(p, p2, p3):
                        for l in range(k + 1, len(primes)):
                            p4 = primes[l]
                            if is_compatible(p, p2, p3, p4):
                                for m in range(l + 1, len(primes)):
                                    p5 = primes[m]
                                    if is_compatible(p, p2, p3, p4, p5):
                                        final_sum = p + p2 + p3 + p4 + p5
                                        print(p, p2, p3, p4, p5)
                                        print("Sum:", final_sum)
                                        return  # Exit after first valid set found

get_primes(limit)
generate_families(primeslist)