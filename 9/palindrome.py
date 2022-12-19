"""
Problem 9
https://leetcode.com/problems/palindrome-number/
"""


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    original_num = x
    stack = 0
    while x > 0:
        remainder = x % 10
        stack = stack * 10 + remainder
        x = x // 10

    return original_num == stack


for num in [1001, 121, -121, 4556554]:
    print(f"{num}: {isPalindrome(num)}")
