from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mapping = defaultdict(int)
        for num in nums:
            mapping[num] += 1

        return [
            number
            for number, _ in sorted(
                mapping.items(),
                key=lambda x: x[1],
                reverse=True,
            )
        ][:k]
