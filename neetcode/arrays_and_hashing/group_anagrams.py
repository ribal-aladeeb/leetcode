"""
problem statement:
https://neetcode.io/problems/anagram-groups?list=neetcode150
"""

from collections import defaultdict


def solution(strs: list[str]) -> list[list[str]]:
    def groupAnagrams(strs: list[str]) -> list[list[str]]:
        if len(strs) <= 1:
            return [strs]

        groups = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            groups[sorted_word].append(word)

        return list(groups.values())
