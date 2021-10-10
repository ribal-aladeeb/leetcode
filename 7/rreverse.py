'''
problem 7
https://leetcode.com/problems/reverse-integer/
'''


def r(x: int) -> int:
    i = 10
    if x < 0:
        sign = -1
        x = x*-1
    else:
        sign = 1

    next_remainder = x % i
    current_remainder = -1
    newest = 0
    reverse = 0
    while (x*10 // i > 0):
        current_remainder = next_remainder
        newest = current_remainder // (i//10)
        reverse = reverse*10 + newest
        i *= 10
        next_remainder = x % i


    reverse = sign*reverse

    if reverse < -2**31 or reverse > 2**31-1:
        return 0

    return reverse




def slow_solution(x: int) -> int:
    '''This solution solves the problem using strings which is probably slow'''
    sign = -1 if x < 0 else 1
    s = str(x*sign)
    return sign * int(s[::-1])


print(r(5670123))
