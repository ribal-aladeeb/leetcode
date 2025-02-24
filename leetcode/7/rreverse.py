"""
problem 7
https://leetcode.com/problems/reverse-integer/
"""


def r(x: int) -> int:
    original_number = x
    i = 10
    if x < 0:
        sign = -1
        x = x * -1
    else:
        sign = 1

    newest = 0
    reverse = 0
    while sign * original_number * 10 // i > 0:
        newest = x % 10
        reverse = reverse * 10 + newest
        x = x // 10
        i *= 10

    reverse = sign * reverse

    if reverse < -(2**31) or reverse > 2**31 - 1:
        return 0

    return reverse


def slow_solution(x: int) -> int:
    """This solution solves the problem using strings which is probably slow"""
    sign = -1 if x < 0 else 1
    s = str(x * sign)
    return sign * int(s[::-1])
