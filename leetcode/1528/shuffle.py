from typing import List


def solution(nums1: List[int], nums2: List[int]) -> float:
    i, j = 0, 0
    merged = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    if i < len(nums1):
        merged += nums1[i:]
    elif j < len(nums2):
        merged += nums2[j:]

    N = len(merged)
    if N % 2 == 0:
        median = (merged[N/2] + merged[N/2-1])/2
    else:
        median = merged[N//2]
    
    return median
