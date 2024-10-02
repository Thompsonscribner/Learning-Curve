import math

primefactors = list()

def is_prime(x):
    for b in range(2, int(math.sqrt(x)) + 1):
        if x % b == 0: return False
        else: continue
    return True

def factor(x):
    for b in range(2, int(math.sqrt(x))+1):
        if x % b == 0:
            primefactors.append(b)
            if is_prime(x/b) == True:
                primefactors.append(int(x/b))
            else:
                x = int(x/b)
                if x % b == 0:
                    primefactors.append(b)
                if is_prime(x/b) == True:
                    primefactors.append(int(x/b))


for a in range(2, 11):
    if is_prime(a) == True: 
        primefactors.append(a)
    else: 
        factor(a)
        continue
print(primefactors)

newdict = dict()
for f in primefactors:
    if f in newdict.keys():
        update = {f : newdict.get(f) + 1}
        newdict.update(update)
    if f not in newdict.keys(): newdict[f] = 1
    
print(newdict)

multlist = list()
for (k, v) in newdict.items():
    mult = k**v
    multlist.append(mult)
print(multlist)

finalnum = 1
for x in multlist:
    finalnum = finalnum*x
print(finalnum)
quit()

        















def check20(x) :
    if not x%2 == 0: return
    if not x%3 == 0: return
    if not x%4 == 0: return
    if not x%5 == 0: return
    if not x%6 == 0: return
    if not x%7 == 0: return
    if not x%8 == 0: return
    if not x%9 == 0: return
    if not x%10 == 0: return
    if not x%11 == 0: return
    if not x%12 == 0: return
    if not x%13 == 0: return
    if not x%14 == 0: return
    if not x%15 == 0: return
    if not x%16 == 0: return
    if not x%17 == 0: return
    if not x%18 == 0: return
    if not x%19 == 0: return
    if not x%20 == 0: return
    else: 
        print(x)
        quit()
quit()
for b in range(2550, 999999):
    check20(b)
print("none found")