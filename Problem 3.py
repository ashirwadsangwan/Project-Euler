'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
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
