class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        zeros = set()
        for idx, num in enumerate(nums):
            if num == 0:
                zeros.add(idx)
            else:
                product *= num

        if len(zeros) > 1:
            return [0] * len(nums)

        for idx, num in enumerate(nums):
            if num == 0:
                nums[idx] = product
            elif len(zeros) == 1:
                nums[idx] = 0
            else:
                nums[idx] = product // num

        return nums
