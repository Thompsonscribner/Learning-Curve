import math
bnum = 600851475143
pfacs = list()
largestpfac = 0
#while True:
 #   if bnum % 2 == 0:

for x in range(2, int(math.sqrt(bnum))+1):
    while True: 
        if bnum % x == 0:
            pfacs.append(x)
            bnum = bnum / x
        else: break

if bnum>1:
    pfacs.append(bnum)

largestpfac = max(pfacs)


print(pfacs)
print(largestpfac)
print("done")

