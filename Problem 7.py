'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
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

## ALTERNATIVE WAY

def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
                break
        else:
            counter += 1
        if counter == n:
            return i

print(nth_prime(10001))
