"""
https://leetcode.com/problems/zigzag-conversion/
"""


def solution(s: str, numRows: int):
    word = s

    rows = [""] * numRows

    i = 0

    while i < len(word):
        for forward_iter in range(numRows):
            if i >= len(word):
                break
            rows[forward_iter] += word[i]
            i += 1

        for backward_iter in reversed(range(1, numRows - 1)):
            if i >= len(word):
                break
            rows[backward_iter] += word[i]
            i += 1

    return "".join(rows)


print(solution("a", 1))
