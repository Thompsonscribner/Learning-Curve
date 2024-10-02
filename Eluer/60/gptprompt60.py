from sympy import isprime
from itertools import combinations

# Check if two primes concatenated in any order remain prime
def is_valid_pair(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))

# Recursive function to find the prime set
def find_prime_set(primes, current_set, size):
    if len(current_set) == size:
        return current_set

    for p in primes:
        if all(is_valid_pair(p, q) for q in current_set):
            new_set = current_set + [p]
            result = find_prime_set(primes, new_set, size)
            if result:
                return result
    return None

# Generate a list of primes up to a certain limit
def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        if isprime(num):
            primes.append(num)
    return primes

def main():
    prime_limit = 10000  # Adjust the limit as necessary
    primes = generate_primes(prime_limit)

    # Find the set of 5 primes that satisfy the condition
    prime_set = find_prime_set(primes, [], 5)

    if prime_set:
        print("Prime set:", prime_set)
        print("Sum:", sum(prime_set))
    else:
        print("No valid set found.")

if __name__ == "__main__":
    main()