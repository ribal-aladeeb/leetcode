# def solution(nums: list[str]) -> list[list[int]]:
#     value2index = {}
#     for idx, value in enumerate(nums):
#         value2index[value] = value2index.get(value, []) + [idx]

#     triplets = set()

#     skip_condition = set()

#     for i in len(nums) - 2:
#         for j in (i + 1, len(nums) - 1):
#             potential_value = (nums[i] + nums[j]) * (-1)

#             if potential_value in value2index and potential_value not in skip_condition:
#                 potential_indices = list(
#                     set(
#                         [k for k in value2index.get(potential_value) if k not in [i, j]]
#                     )
#                 )
#                 for k in potential_indices:
#                     triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))

#                 skip_condition.add(potential_value)

#     return list(triplets)


# print(solution(nums=[-1, 0, 1, 2, -1, -4]))


def optimized(nums: list[int]) -> list[list[int]]:
    sorted_nums = sorted(nums)
    mapping = {}
    for idx, value in enumerate(sorted_nums):
        mapping[value] = mapping.get(value, []) + [idx]

    i, k = 0, len(sorted_nums) - 1
    solutions: set[tuple] = set()
    while i < k - 1:
        potential_complement = (sorted_nums[i] + sorted_nums[k]) * (-1)
        if potential_complement in mapping:
            # find an index j != i != k
            potential_Js = set(mapping[potential_complement])
            potential_Js.discard(i)
            potential_Js.discard(k)
            if len(potential_Js) > 0:
                solutions.add(
                    tuple(
                        sorted(
                            [
                                sorted_nums[i],
                                potential_complement,
                                sorted_nums[k],
                            ]
                        )
                    )
                )

        if (i + k) % 2 == 0:
            i += 1
        else:
            k -= 1

    return [list(triplet) for triplet in solutions]


# print(optimized([-1, 0, 1, 2, -1, -4]))


def optimal2(nums: list[int]) -> list[list[int]]:
    sorted_nums = sorted(nums)
    solutions = set()
    for i in range(len(nums) - 3):
        j = i + 1
        k = len(nums) - 1
        target = -sorted_nums[i]
        while j < k:
            complement = sorted_nums[j] + sorted_nums[k]
            if complement == target:
                solutions.add(
                    tuple(sorted([sorted_nums[i], sorted_nums[j], sorted_nums[k]]))
                )
                i += 1
                k -= 1
            elif complement < target:
                i += 1
            else:
                k -= 1
    return [list(triplet) for triplet in solutions]
