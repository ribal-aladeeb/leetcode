class Solution:
    def longestConsecutive(nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        seen = set(nums)
        max_length = 1
        for num in seen:
            i = 1
            if (num - 1) not in seen:
                while num + i in seen:
                    i += 1
                max_length = max(max_length, i)
        return max_length
