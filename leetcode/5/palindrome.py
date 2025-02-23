
from collections import defaultdict
# 5. Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.

# def longest_palindrome(s):


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(any_str):
            if len(any_str) <= 0:
                raise Exception("empty imput palindrome")
            lower = 0
            upper = len(any_str)-1

            while(lower < upper):
                leftmost = any_str[lower]
                rightmost = any_str[upper]
                if (leftmost != rightmost):
                    return False
                lower += 1
                upper -= 1

            return True

        if len(s) < 1:
            return s

        longest = s[0]
        for start in range(len(s)-1):
            for end in range(start+1, len(s)):
                if len(longest) == len(s):
                    return longest
                substring = s[start:end+1]
                isPal = is_palindrome(substring)
                if (isPal and len(longest) < len(substring)):
                    longest = substring

        return longest


x = "helloollsdv"
sol = Solution()
print(sol.longestPalindrome(x))


def longest(word: str):
    letters = defaultdict(list)

    for i in range(len(word)):
        letters[word[i]].append(i)

    palindromes = []
    bound = -1
    for i in range(len(word)):
        occurrences= len(letters[word[i]])
        if occurrences <1:
            raise Exception("you not supposed to have less than 1 occurrence you dumb arm pit")

        elif occurrences == 1:
            continue

        elif occurrences ==2:
