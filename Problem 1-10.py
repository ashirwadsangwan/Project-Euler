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



## Problem 8

x = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
gr_product_13 = 0
for i in range(len(x)-12):
    if gr_product_13 < (int(x[i])*int(x[i+1])*int(x[i+2])*int(x[i+3])*int(x[i+4])*int(x[i+5])*int(x[i+6])*int(x[i+7])*int(x[i+8])*int(x[i+9])*int(x[i+10])*int(x[i+11])*int(x[i+12])):
        gr_product_13 = (int(x[i])*int(x[i+1])*int(x[i+2])*int(x[i+3])*int(x[i+4])*int(x[i+5])*int(x[i+6])*int(x[i+7])*int(x[i+8])*int(x[i+9])*int(x[i+10])*int(x[i+11])*int(x[i+12]))
        
gr_product_13 




## Problem 9

for a in range(1,1000):
    for b in range(1,999):
        c = 1000 - (a+b)
        if c**2 == (b**2 + a**2):
            print(a*b*c)
            print(a,b,c)

            
            
## Problem 10

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum
