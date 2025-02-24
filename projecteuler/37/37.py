'''
https://projecteuler.net/problem=37
'''

def is_prime(n:int) -> bool:
    if n == 1:
        return False
    
    square_root_of_n = int(n**(1/2)+1)
    for i in range(2,square_root_of_n):
        if n % i == 0:
            return False
    return True


def generate_next_prime():
    i = 10
    while True:
        i+=1
        # print(i)
        if is_prime(i):
            yield i

def truncatable(prime: int)->bool:
    stringified: str = str(prime)

    # truncate from the left
    for i in range(1, len(stringified)):
        truncated = int(stringified[i:len(stringified)])
        if not is_prime(truncated):
            return False
    
    # truncate from the right
    for i in range(len(stringified)-1, 0, -1):
        truncated = int(stringified[0:i])
        if not is_prime(truncated):
            return False
    
    return True




def find_truncatable_primes()-> list[int]:
    number_of_primes_analyzed = 0
    truncatable_primes = []
    for prime in generate_next_prime():
        number_of_primes_analyzed+=1
        # print(f'\r{number_of_primes_analyzed}')
        if truncatable(prime):
            print(f"found truncatable prime {prime}, primes analyzed so far: {number_of_primes_analyzed}")
            truncatable_primes.append(prime)
        if len(truncatable_primes) >= 11:
            return truncatable_primes
    
truncatables = find_truncatable_primes()
print(truncatables)
print(sum(truncatables))



        

