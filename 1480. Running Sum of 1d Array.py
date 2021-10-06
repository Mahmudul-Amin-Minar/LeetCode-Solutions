def runningSum(nums):
    for i, num in enumerate(nums):
        if i == 0:
            continue
        else:
            nums[i] = nums[i] + nums[i-1]
    return nums

print(runningSum([3,1,2,10,1]))
