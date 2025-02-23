def removeDuplicates(nums):
    hashmap = {}
    for i in reversed(range(len(nums))):
        try:
            hashmap[nums[i]]
            del nums[i]
        except:
            hashmap[nums[i]] = True
    return len(nums)

yo = [1,2,2,2,5,4,4,1,1]

print(removeDuplicates(nums=yo))
print(yo)
