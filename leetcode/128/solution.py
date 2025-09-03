"""
Problem 128
https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=problem-list-v2&envId=oizxjoit
"""

from logging import Logger
from collections import OrderedDict


def longestConsecutive(nums: list[int], level=Logger.info) -> int:
    print(f"\n******* finding consecutives or {nums}")
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    unique = set(nums)
    print("built set of unique values")
    print(unique)
    smallest = nums[0]
    largest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n
    print("identified min and max values")
    print(smallest, largest)

    consecutives = set()
    consecutives.add(1)
    has_consecutive = (
        {}
    )  # maps any given number x to the number of consecutives that exist in x-1, x-2, x-3, ...
    buffer = 1

    for x in unique:
        if x - 1 in unique:
            y = x - 1
            while y in unique:
                pass

    # ---------------------- working algo 1 (brute force) ----------------------
    # for x in sorted(unique):
    #     consecutives_found = x in unique and x - 1 in unique
    #     if consecutives_found:  # i-1 and i are exist in unique
    #         buffer += 1
    #     else:
    #         consecutives.add(buffer)
    #         buffer = 1
    #     print(f"{x} and {x-1} in unique:{consecutives_found}, buffer: {buffer}")
    #    consecutives.add(buffer)
    # print(consecutives)
    # return max(consecutives)
    # ---------------------- ---------------------- ----------------------


cases = (
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [1, 0, 1, 2],
    [1, 2, 3, 4],
    [-2, -1, 0, 1, 5, 6, 7, 8, 9, 11, 20],
    [-1, 0, 1, 5, 20, 7, 8, 9, 11, 6, -2],
)

matrix = [(c, longestConsecutive(c)) for c in cases]
print()
for input, output in matrix:
    print()
    print(input, output)
