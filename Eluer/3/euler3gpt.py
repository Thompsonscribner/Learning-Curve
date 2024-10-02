import math

bnum = 600851475143
pfacs = list()
largestpfac = 0

for x in range(2, int(math.sqrt(bnum)) + 1):  # Only iterate up to sqrt(bnum)
    while bnum % x == 0:
        pfacs.append(x)
        bnum = bnum // x  # Use integer division to avoid floating-point errors

if bnum > 1:  # If there is a remaining prime factor larger than sqrt(bnum)
    pfacs.append(bnum)

largestpfac = max(pfacs)

print(pfacs)
print(largestpfac)
print("done")