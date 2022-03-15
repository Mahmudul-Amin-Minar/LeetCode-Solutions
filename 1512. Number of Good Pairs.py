def numIdenticalPairs(nums) -> int:
    l = len(nums)
    pair = 0
    for i in range(0, l):
        for j in range(i+1, l):
            if nums[i] == nums[j]:
                pair += 1
    return pair