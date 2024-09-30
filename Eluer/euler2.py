fib = list()
fibeven = list()
n= 0
nlast1 = 1
nlast2 = 0 
while n <4000000:
    n = nlast1 +nlast2 
    fib.append(n)
    nlast2 = nlast1
    nlast1 = n

for x in fib:
    if x % 2 == 0:
        fibeven.append(x)
    else: continue

print (sum(fibeven))
