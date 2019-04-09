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


## Problem 5

for i in range(1,300000000):
    if i%2==0 and i%3==0 and i%4==0 and i%5==0 and i%6==0 and i%7==0 \
    and i%8==0 and i%9==0 and i%10==0 and i%11==0 and i%12==0 and i%13==0\
    and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0 and i%20==0:
        print(i)
    

    
## Problem 6

def dif_ss(a,b):
    sum_squares = 0
    for i in range(a,b):
        sum_squares+=i**2

    sum_ = 0
    for j in range(a,b):
        sum_ += j
    square_of_sum = sum_**2
    
    return square_of_sum - sum_squares

print(dif_ss(1,101))

## Problem 7

def prime_array(a,b):
    prime_list=[]

    for num in range(a, b+1):

        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list  

# n*np.log(n) + n(np.log(np.log(n))-1) < 10001 < n*np.log(n) + n*np.log(np.log(n))
# which gives us 10001st prime is between 104318 and 114320

prime_array(1,114320)[10000]
