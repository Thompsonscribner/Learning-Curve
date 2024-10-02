n = 0
nums = list()
while n<1000:
    if (n % 3 == 0):
        nums.append(n)
        n = n + 1
        continue
    if (n%5 == 0): 
        nums.append(n)
        n = n +1 
        continue
    else:
        n = n +1
        continue
print(sum(nums))
