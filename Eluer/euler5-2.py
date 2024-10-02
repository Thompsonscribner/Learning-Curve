import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

# Finding the smallest positive number evenly divisible by all numbers from 1 to 20
numbers = range(1, 21)
smallest_number = lcm_multiple(numbers)
print(smallest_number)