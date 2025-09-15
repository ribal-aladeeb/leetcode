"""
Problem statement:
https://neetcode.io/problems/is-anagram?list=neetcode150
"""

from collections import defaultdict


def solution(s: str, t: str) -> bool:
    def isAnagram(s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):

            s_map[s[i]] += 1
            t_map[t[i]] += 1

        for letter in s_map:
            if letter not in t_map or s_map[letter] != t_map[letter]:
                return False

        return True
