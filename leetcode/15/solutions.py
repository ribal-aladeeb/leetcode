def solution(nums: list[str]) -> list[list[int]]:
    value2index = {}
    for idx, value in enumerate(nums):
        value2index[value] = value2index.get(value, []) + [idx]

    triplets = set()

    skip_condition = set()

    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            potential_value = (nums[i] + nums[j]) * (-1)

            if potential_value in value2index and potential_value not in skip_condition:
                potential_indices = list(
                    set(
                        [k for k in value2index.get(potential_value) if k not in [i, j]]
                    )
                )
                for k in potential_indices:
                    triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

                skip_condition.add(potential_value)

    return list(triplets)


print(solution(nums=[-1, 0, 1, 2, -1, -4]))


def optimized(nums: list[int]) -> list[list[int]]:
    pass
