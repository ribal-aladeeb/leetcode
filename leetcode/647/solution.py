"""
https://leetcode.com/problems/palindromic-substrings/?envType=problem-list-v2&envId=oizxjoit
"""


def is_palindrome(s: str) -> bool:
    offset = 0
    while offset <= (len(s) - offset - 1):
        if s[offset] != s[-1 - offset]:
            return False
        offset += 1
    return True


def solution(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    palindrome_cache = {}
    palindrome_counter = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring not in palindrome_cache:
                palindrome_cache[substring] = is_palindrome(substring)
            palindrome_counter += palindrome_cache[substring]
    return palindrome_counter
