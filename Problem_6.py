'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385 The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025 Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def dif_ss(a,b):
    sum_squares = 0
    for i in range(a,b):
        sum_squares+=i**2

    sum_ = 0
    for j in range(a,b):
        sum_ += j
    square_of_sum = sum_**2
    
    return square_of_sum - sum_squares


if __name__ == '__main__':
    dif_ss(1,101)
