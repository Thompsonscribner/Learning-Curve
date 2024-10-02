import math
from itertools import combinations

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate a list of primes up to a limit using the Sieve of Eratosthenes
def generate_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for i in range(start * start, limit, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Function to find smallest prime that generates a family of 8 primes
def find_smallest_prime_in_family(prime_list):
    for prime in prime_list:
        prime_str = str(prime)
        num_digits = len(prime_str)
        
        # Try replacing 1, 2, ... (num_digits - 1) digits of the prime
        for num_replaced_digits in range(1, num_digits):
            # Generate all combinations of digit positions to replace
            for digit_positions in combinations(range(num_digits), num_replaced_digits):
                prime_family = []
                
                # Replace the digits at these positions with digits 0-9
                for digit in '0123456789':
                    candidate = list(prime_str)
                    
                    # Replace selected positions with the same digit
                    for pos in digit_positions:
                        candidate[pos] = digit
                    
                    # Avoid leading zeros
                    if candidate[0] != '0':
                        candidate_num = int(''.join(candidate))
                        if is_prime(candidate_num):
                            prime_family.append(candidate_num)
                
                # Check if we have a family of 8 primes
                if len(prime_family) == 8:
                    return min(prime_family)

# Main function to solve the problem
def main():
    # Generate primes up to a reasonable limit
    limit = 1000000  # We can adjust this based on the problem's difficulty
    primes = generate_primes(limit)
    
    # Find the smallest prime in the family of 8 primes
    result = find_smallest_prime_in_family(primes)
    print("The smallest prime in an eight prime value family is:", result)

if __name__ == "__main__":
    main()
