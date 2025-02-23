from typing import List


def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    char = {}
    for character in allowed:
        char[character] = 1

    total = 0
    for word in words:
        matches = [char.get(letter, -1) for letter in word]
        if len(matches) == sum(matches):
            total += 1

    return total
