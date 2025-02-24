'''
https://projecteuler.net/problem=25
'''
from math import sqrt, pow
from sys import argv
def fib(n: int):
    '''returns the Nth fibonacci number using closed form'''
    term1 = int(pow((1+sqrt(5))/2),n)
    term2 = int(((1-sqrt(5))/2)**n)
    return int((term1 - term2)/sqrt(5))

    # return (term1**n - term2**n)/sqrt(5)


# print(fib(int(argv[1])))

def fib_iter():
    '''return the Nth fibonnaci number iteratively'''
    n_2 = 1
    n_1 = 1
    i = 2
    fib = 0
    while True:
        fib = n_1 + n_2
        n_2 = n_1
        n_1 = fib
        i+=1
        if len(str(fib))==15000:
            return i, fib


print(fib_iter())
        
        

