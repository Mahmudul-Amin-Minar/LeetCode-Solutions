def twoSum(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i] + nums[j] == target:
                return [i, j]

print(twoSum([2,5,5,11], 10))