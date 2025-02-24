from itertools import combinations


def pal(s):
    for size in reversed(range(1, len(s) + 1)):
        for i in range(len(s) - size + 1):
            # the +1 is for the edge case where there is no palindrome
            candidate = s[i : i + size]
            if candidate == candidate[::-1]:
                return candidate


def sami(s):
    def is_palind(s):
        return s == s[::-1]

    largest_yet = ""
    indices = {}  # key is a character, values is a list of indices
    for i in range(len(s)):
        indices[s[i]] = indices.get(s[i], ()) + (i,)

    number_of_repeated_letters = 0
    for letter in indices:
        number_of_repeated_letters += 1 if len(indices[letter]) > 1 else 0
        if len(indices[letter]) > 1:
            combis = list(combinations(indices[letter], 2))
            for comb in combis:
                if comb[1] - comb[0] + 1 > len(largest_yet) and is_palind(
                    s[comb[0] : comb[1] + 1]
                ):
                    largest_yet = s[comb[0] : comb[1] + 1]

    if number_of_repeated_letters == 0:
        return s[0]

    return largest_yet


test_cases = {
    "babad": "bab",
    "a": "a",
    "ac": "a",
}

for t in test_cases:
    print(f"{t}: {sami(t)}")
