def maxAscendingSum(nums) -> int:
    maxSum = 0
    current_sum = 0
    l = len(nums)
    for i in range(0, l):
        if i==0 or nums[i-1] < nums[i]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        maxSum = max(maxSum, current_sum)
    return maxSum

print("sum", maxAscendingSum([10,20,30,40,50]))