"""
Leetcode problem 17
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

from itertools import product
from sys import argv

def letterCombinations(digits: str) -> list[str]:

    letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    combinations = []
    for d in digits:
        if not combinations:
            combinations = letters[d]
        else:
            combinations = ["".join(p) for p in product(combinations, letters[d])]

    return combinations


letterCombinations(argv[1])