import math

amicables = list()
pdivs = list()
#prime factorization function
def proper_divs(b):
    pdivs.clear()
    for x in range(int(1), int(b/2)+1):  # Only iterate up to sqrt(bnum)
        if b % x == 0:
            pdivs.append(x)
    return pdivs


for a in range(1, 10001):
    b = sum(proper_divs(a))  # Get sum of divisors of 'a'
    if b > a and b <= 10000:  # Ensure b is a valid number greater than a
        if sum(proper_divs(b)) == a:  # Check if sum of divisors of 'b' is 'a'
            amicables.append((a, b))

print(amicables)
sumlist = list()
for a, b in amicables: 
    sumlist.append(a+b)
print(sum(sumlist))