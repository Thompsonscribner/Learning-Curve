#is a palindrome
paldict = dict()
def is_palindrome(x):
    forward = str(x)
    backward = "".join(reversed(forward))
    if forward == backward: return True
    else: return False

for a in range (900, 1000):
    for b in range(900, 1000):
        if is_palindrome((a*b)) == True: paldict[(a,b)] = (a*b)
        else: continue

biggest = 0
for pal in paldict.values():
    if pal > biggest: biggest = pal
    else: continue
print (biggest)
print(paldict)
