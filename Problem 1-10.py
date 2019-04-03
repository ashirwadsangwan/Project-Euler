## Problem 1

sum = 0
for i in range(1000):
    if i%3==0 or i%5==0:
        sum += i
        
        
## Problem 2

def fib_till(n):
    fib_till = [1,2]
    
    for i in range(2, n+1):
        fib_till.append(fib_till[-1] + fib_till[-2])
    
    return fib_till

sum_even_fib = 0
for i in fib_till(32):
    if i%2==0:
        sum_even_fib += i
        
print(sum_even_fib)


## Problem 3

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(np.sqrt(n)) + 1, 2))
        
prime_factors = []

for i in range(2,775146):
    if is_prime(i)==True:
        if (600851475143)%i==0:
            prime_factors.append(i)

prime_factors[-1] 

## Problem 4


    
