import math

def is_prime(n):
    x = int(n)
    for a in range(2, math.floor(math.sqrt(x))+1):
        if x % a == 0: return False
    return True

rplist = list()
smalllist = list()

def one_digit(digit):
    global smalllist
    for a in range(100000, 1000000):
        stra = str(a)
        rplist.clear()
        n = str(0)
        for b in stra:
            while int(n)<10:
                rplist.append(stra.replace(stra[digit], n))
                n = str(int(n) + 1)
        count = 0
        for entry in rplist: 
            if is_prime(entry)==True : count = count + 1
        #print("primes=", count)
        if count == 8: 
            print("found one")
            if not smalllist: 
                smalllist = rplist.copy()
            if (int(rplist[0])) < (int(smalllist[0])):
                smalllist = rplist.copy()
                print("new smallest: ", smalllist)
        #print(rplist)

for c in range(1, 7):
    one_digit(c)

print(smalllist)