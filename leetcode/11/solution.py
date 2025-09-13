"""
https://leetcode.com/problems/container-with-most-water/description/?envType=problem-list-v2&envId=oizxjoit
"""


def brute_force_solution(height: list[int]) -> int:
    max_area = 0
    for i in range(len(height)):
        for j in range(len(height), i, -1):
            area = min()
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
    return max_area


def linear_solution(height: list[int]) -> int:
    # first make a dict mapping heights to their index in the original list

    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        B = right - left
        H = min(height[left], height[right])
        area = B * H
        max_area = max(max_area, area)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area
